#!/usr/bin/python
# Jussi Sarkkinen 2012
# This 
import sys

len(sys.argv) == 2 or sys.exit('Missing input file name.')
f = file(sys.argv[1])
print '''
<html>
<head>
        <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=ISO-8859-1">
        <script src="sorttable.js"></script> 
        <script>
        function load() {
                sorttable.innerSortFunction.apply(document.getElementById("candidate_p"), []);
                sorttable.innerSortFunction.apply(document.getElementById("candidate_p"), []);
        }
        </script>
</head>
<style type="text/css">
table.sample {
        border-width: thin;
        border-spacing: 0px;
        border-style: none;
        border-color: black;
        border-collapse: collapse;
        background-color: white;
}
table.sample th {
        border-width: thin;
        padding: 2px;
        border-style: solid;
        border-color: gray;
        background-color: white;
        -moz-border-radius: ;
}
table.sample td {
        border-width: thin;
        padding: 2px;
        border-style: solid;
        border-color: gray;
        background-color: white;
        -moz-border-radius: ;
        text-align: right;
}
</style>
<body onload="load()">
<table class="sortable sample">
'''

headers = {}

for line in f:
    print "<tr>"
    items = line.rstrip().split("\t")
    i = 0
    for item in items:
        if not i in headers:
            headers[i] = item
            print "<th id='%s'>%s</th>" % (headers[i], item)
        else:
            print "<td id='%s'>%s</td>" % (headers[i], item)
        i += 1
    print "</tr>"

print "</table>"
print "</body></html>"
