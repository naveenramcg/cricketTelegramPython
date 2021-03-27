from pycricbuzz import Cricbuzz
import json


c = Cricbuzz()

def get_matches():
    matches = c.matches()
    #print(matches)
    i = 1
    mat = ''
    for item in matches:
        s = (str(i) + ". " + item['srs'])
        mat = mat + '\n' + str(s)
        i = i + 1
    return mat
def current_match_number():
    matches = c.matches()
    #print(len(matches))
    return len(matches)
#print(get_matches())
#print(current_match_number()+1)

#mat = get_matches()
#print(mat)
def get_score(num):
    match = c.matches()
    score = c.livescore(match[num-1]['id'])
    sc=match[num-1]['srs']+ "\nBatting:" +score['batting']['team']+ "\nInnings Number: "+score['batting']['score'][0]['inning_num'] + "\nRuns: "+score['batting']['score'][0]['runs']+"\tWickets Lost: "+ score['batting']['score'][0]['wickets']+ "\t\tOvers: " + score['batting']['score'][0]['overs']+"\n"+str(score['batting']['batsman'][0])+"\n"+str(score['batting']['batsman'][1])+"\nBowling:"+score['bowling']['team']+"\nInnings Number: "+score['bowling']['score'][0]['inning_num'] + "\nRuns: "+score['bowling']['score'][0]['runs']+"\tWickets Lost: "+ score['bowling']['score'][0]['wickets']+ "\t\tOvers: " + score['bowling']['score'][0]['overs']+"\n"+str(score['bowling']['bowler'][0])
    return sc

#print(get_score(1))
#current_match_number()