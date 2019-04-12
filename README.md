# retrieve-google-competition-results

Description

## Usage

    # order user per score for one country
    # x is a loaded json result
    sorted([(u['displayname'], str(u['score_1'])) for u in x['user_scores'] if u['country'] == 'France'], key=lambda x: x[1])
