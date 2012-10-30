#!/usr/bin/python
# coding=utf8
# Download YLE election data and create candidate/area result table.
# Jussi Sarkkinen 2012

import re, sys
from urllib import urlopen

PARTY="VIHR"

BASE_URL="http://vaalit.yle.fi/tulospalvelu/2012/kuntavaalit/kunnat/aanestysalueet/helsinki_aanestysalue_puolueet_1_91_%s.html"

def munchline(line):
    return int(re.findall(r'.*\>(.+)\<', line)[0].replace(' ', ''))

def main(argv):
    if len(argv) != 1:
          sys.exit("Missing input file name. File should contain tab separated area code, name and vote counts.\nE.g. copy paste from http://vaalit.yle.fi/tulospalvelu/2012/kuntavaalit/ehdokkaat/ehdokas_1_91_954.html.")

    areafile = argv[0]
    areas=[]
    with open(areafile, 'rU') as f:
        for line in f:
            areas.append( line.rstrip().split('\t') )

    print "Koodi\tAlueen nimi\tÄänioikeutettuja\tÄäniä\tPuolueen ääniä\tEhdok. ääniä\tAktiivisuus\tPuolueen %\tEhdok. %\tEhdok. % puolueen äänistä"

    for area in areas:
        URL = BASE_URL % area[0]

        party = 0
        content = urlopen(URL)
        target = ''
        parsed = {}
        for line in content:
            if target:
                parsed[target] = munchline(line)
                target = ''
            elif PARTY in line:
                target = 'party'
            elif "oikeutettuja" in line:
                target = 'voters'
            elif "Hyv" in line:
                target = 'votes'
        
        a_code = area[0]
        a_name = area[1]
        a_candidate = int(area[2])
        party = parsed['party']
        votes = parsed['votes']
        voters = parsed['voters']
        
        a_party_p = party*100.0/votes
        a_activ_p = votes*100.0/voters
        a_candidate_p = a_candidate*100.0/votes
        a_candidate_party_p = a_candidate*100.0/party
    
        print "%s\t%s\t%d\t%d\t%d\t%d\t%.2f%%\t%.2f%%\t%.2f%%\t%.2f%%" % (a_code, a_name, voters, votes, party, a_candidate, a_activ_p, a_party_p, a_candidate_p, a_candidate_party_p)

if __name__ == "__main__":
    main(sys.argv[1:])
