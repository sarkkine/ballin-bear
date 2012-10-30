ballin-bear
===========

Election result scraping tool. Will pull data from YLE election result pages and output
voting activity, candidate support percentages per area and in comparison to party votes in that area.
Currently configured for VIHR candidates, can be changed in the kannatus.py file

For example output, see: http://dl.dropbox.com/u/5740841/otso_results.html

Before running you need to copy and paste candidate's data from YLE to a source file, 
from e.g. http://vaalit.yle.fi/tulospalvelu/2012/kuntavaalit/ehdokkaat/ehdokas_1_91_954.html.

Example usage:

```
python kannatus.py example/otso_alueet.txt > otso_results.tsv
python tsv_to_html.py otso_results.txv > otso_results.html
```

Host the resulting html file and example/sorttable.js somewhere, and off you go.

See example directory for source and result files. 

This is free and unencumbered public domain software. Do whatever you want with it.
For more information, see http://unlicense.org/.


TODO:

- Make it pull also initial data from web
- Party setting from command line :)