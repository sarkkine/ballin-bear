ballin-bear
===========

Election result scraping tool. Will pull data from YLE election result pages.

For example output, see: http://dl.dropbox.com/u/5740841/otso_results.html

Example usage:

```
./kannatus.py example/otso_alueet.txt > otso_results.tsv
./tsv_to_html.py otso_results.txv > otso_results.html
```

Host the resulting html file and example/sorttable.js somewhere, and off you go.

See example directory for source and result files. 

This is free and unencumbered public domain software. Do whatever you want with it.
For more information, see http://unlicense.org/.

