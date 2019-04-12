import logging
import requests
import base64
import json
import re
import os


logger = logging.getLogger(__name__)


def decode(encoded):
    clean = re.sub(r'/[^A-Za-z0-9+/]/g', "", encoded.replace("-", "+")
                                                    .replace("_", "/"))
    clean += '=' * (-len(clean) % 4)
    return json.loads(base64.b64decode(clean))

def encode(value):
    return re.sub(r'/[^A-Za-z0-9+/]/g', "",
                  base64.b64encode(json.dumps(value, separators=(',', ':'))
                                       .encode('utf8'))
                        .decode("utf8")
                        .replace("+", "-")
                        .replace("/", "_"))


def get_url(year, round):
    static_map = {
        "2019": {
            "qualification" : "0000000000051705"
        }
    }
    year = str(year)
    round = str(round)
    if not year in static_map or round not in static_map[year]:
        logger.error("unknown mapping from <year={year}, round={round} to url" \
                     .format(year, round))
        sys.exit(1)

    return "https://codejam.googleapis.com/scoreboard/{}".format(
            static_map[year][round])


def create_query_params(start, nb):
    # we cannot retrieve all the results
    assert(nb <= 100)
    return {
        "min_rank": start,
        "num_consecutive_users": nb
    }


def get_results_part(year, round, start, nb):
    params = create_query_params(start, nb)
    encoded_params = encode(params)
    url = "{}/poll?p={}".format(get_url(year, round), encoded_params)
    data = requests.get(url).text
    return decode(data)

def get_results(year, round, start, nb):
    if nb != 0 and nb <= 100:
        res = get_results_part(year, round, start, nb)
    else:
        res = {}
        all = False
        if nb == 0:
            all = True
            nb = 100
        while all or nb > 0:
            if nb > 100:
                n = 100
            else:
                n = nb
            try:
                logger.info("paginating ... {} -> {}".format(start, start + n))
                current_res = get_results_part(year, round, start, n)
            except:
                logger.error("something happened. Damned")
                pass
                break
            if len(res) == 0:
                res = current_res
            else:
                res['user_scores'] += current_res['user_scores']
            if 'full_scoreboard_size' in res and start + n >= res['full_scoreboard_size']:
                break
            start += n
            if not all:
                nb -= n

    return res

def write_results(res, year, round, start, nb, output_dir):
    filename = '{}_{}_{}_{}.json'.format(year, round, start, nb)
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    with open(os.path.join(output_dir,  filename), 'w') as output:
        output.write(json.dumps(res))

def get_write_results(year, round, start, nb, output_dir):
    res = get_results(year, round, start, nb)
    write_results(res, year, round, start, nb, output_dir)
