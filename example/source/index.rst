.. Example documentation master file, created by
	 You can adapt this file completely to your liking, but it should at least
	 contain the root `toctree` directive.

###################################
Welcome to Example's documentation!
###################################

Contents:

.. toctree::
	 :maxdepth: 2

=====
Intro
=====

==================
Step 1. The Signal
==================

.. pywave:: jsonml

	{ "signal": [{ "name": "Alfa", "wave": "01.zx=ud.23.45" }] }

====================
Step 2. Adding Clock
====================

.. pywave:: jsonml

	{ "signal": [
	  	{ "name": "pclk", "wave": "p......." },
	  	{ "name": "Pclk", "wave": "P......." },
	  	{ "name": "nclk", "wave": "n......." },
	  	{ "name": "Nclk", "wave": "N......." },
	  	{},
	  	{ "name": "clk0", "wave": "phnlPHNL" },
	  	{ "name": "clk1", "wave": "xhlhLHl." },
	  	{ "name": "clk2", "wave": "hpHplnLn" },
	  	{ "name": "clk3", "wave": "nhNhplPl" },
	  	{ "name": "clk4", "wave": "xlh.L.Hx" }
	]}

============================
Step 3. Putting all together
============================

.. pywave:: jsonml

	{ "signal": [
	  	{ "name": "clk",  "wave": "P......" },
	  	{ "name": "bus",  "wave": "x.==.=x", "data": ["head", "body", "tail", "data"] },
	  	{ "name": "wire", "wave": "0.1..0." }
	]}

========================
Step 4. Spacers and Gaps
========================

.. pywave:: jsonml

	{ "signal": [
	  	{ "name": "clk",         "wave": "p.....|..." },
	  	{ "name": "Data",        "wave": "x.345x|=.x", "data": ["head", "body", "tail", "data"] },
	  	{ "name": "Request",     "wave": "0.1..0|1.0" },
	  	{},
	  	{ "name": "Acknowledge", "wave": "1.....|01." }
	]}

==================
Step 5. The groups
==================

.. pywave:: jsonml

	{ "signal": [
	  	{    "name": "clk",   "wave": "p..Pp..P"},
	  	["Master",
	  	  	["ctrl",
	  	  	  	{"name": "write", "wave": "01.0...."},
	  	  	  	{"name": "read",  "wave": "0...1..0"}
	  	  	],
	  	  	{  "name": "addr",  "wave": "x3.x4..x", "data": "A1 A2"},
	  	  	{  "name": "wdata", "wave": "x3.x....", "data": "D1"   }
	  	],
	  	{},
	  	["Slave",
	  	  	["ctrl",
	  	  	  	{"name": "ack",   "wave": "x01x0.1x"}
	  	  	],
	  	  	{  "name": "rdata", "wave": "x.....4x", "data": "Q2"}
	  	]
	]}

========================
Step 6. Period and Phase
========================

.. pywave:: jsonml

	{ "signal": [
	  	{ "name": "CK",   "wave": "P.......",                                              "period": 2  },
	  	{ "name": "CMD",  "wave": "x.3x=x4x=x=x=x=x", "data": "RAS NOP CAS NOP NOP NOP NOP", "phase": 0.5 },
	  	{ "name": "ADDR", "wave": "x.=x..=x........", "data": "ROW COL",                     "phase": 0.5 },
	  	{ "name": "DQS",  "wave": "z.......0.1010z." },
	  	{ "name": "DQ",   "wave": "z.........5555z.", "data": "D0 D1 D2 D3" }
	]}

============================
Step 7.The config{} property
============================

Hscale=1
========

.. pywave:: jsonml

	{ "signal": [
	  	{ "name": "clk",     "wave": "p...." },
	  	{ "name": "Data",    "wave": "x345x",  "data": ["head", "body", "tail"] },
	  	{ "name": "Request", "wave": "01..0" }
	  	],
	  	"config": { "hscale": 1 }
	}

Hscale=2
========

.. pywave:: jsonml

	{ "signal": [
	  	{ "name": "clk",     "wave": "p...." },
	  	{ "name": "Data",    "wave": "x345x",  "data": ["head", "body", "tail"] },
	  	{ "name": "Request", "wave": "01..0" }
	  	],
	  	"config": { "hscale": 2 }
	}

Hscale=3
========

.. pywave:: jsonml

	{ "signal": [
	  	{ "name": "clk",     "wave": "p...." },
	  	{ "name": "Data",    "wave": "x345x",  "data": ["head", "body", "tail"] },
	  	{ "name": "Request", "wave": "01..0" }
	  	],
	  	"config": { "hscale": 3 }
	}

Head, foot, tock, text
======================

.. pywave:: jsonml

	{"signal": [
	  	{"name":"clk",         "wave": "p...." },
	  	{"name":"Data",        "wave": "x345x", "data": "a b c" },
	  	{"name":"Request",     "wave": "01..0" }
	],
	"head":{
		"text":"pywave example",
	   	"tick":0
	},
	"foot":{
		"text":"Figure 100",
		"tock":9
	}
	}

H1, h2, h3, h4, h5, h6, muted, warning, error, info, success
============================================================

.. pywave:: jsonml

	{"signal": [
	  	{"name":"clk", "wave": "p.....PPPPp...." },
	  	{"name":"dat", "wave": "x....2345x.....", "data": "a b c d" },
	  	{"name":"req", "wave": "0....1...0....." }
	],
	"head": {"text":
	  	["tspan",
	  	  	["tspan", {"class":"error h1"}, "error "],
	  	  	["tspan", {"class":"warning h2"}, "warning "],
	  	  	["tspan", {"class":"info h3"}, "info "],
	  	  	["tspan", {"class":"success h4"}, "success "],
	  	  	["tspan", {"class":"muted h5"}, "muted "],
	  	  	["tspan", {"class":"h6"}, "h6 "],
	  	  	"default ",
	  	  	["tspan", {"fill":"pink", "font-weight":"bold", "font-style":"italic"}, "pink-bold-italic"]
	  	]
	},
	"foot": {"text":
	  	["tspan", "E=mc",
	  	  	["tspan", {"dy":"-5"}, "2"],
	  	  	["tspan", {"dy": "5"}, ". "],
	  	  	["tspan", {"font-size":"25"}, "B "],
	  	  	["tspan", {"text-decoration":"overline"},"over "],
	  	  	["tspan", {"text-decoration":"underline"},"under "],
	  	  	["tspan", {"baseline-shift":"sub"}, "sub "],
	  	  	["tspan", {"baseline-shift":"super"}, "super "]
	  	],"tock":-5
	}
	}

==============
Step 8. Arrows
==============

Splines
=======

.. pywave:: jsonml

	{ "signal": [
		{ "name": "A", "wave": "01........0....",  "node": ".a........j" },
		{ "name": "B", "wave": "0.1.......0.1..",  "node": "..b.......i" },
		{ "name": "C", "wave": "0..1....0...1..",  "node": "...c....h.." },
		{ "name": "D", "wave": "0...1..0.....1.",  "node": "....d..g..." },
		{ "name": "E", "wave": "0....10.......1",  "node": ".....ef...." }
		],
		"edge": [
			"a~b t1", "c-~a t2", "c-~>d time 3", "d~-e",
			"e~>f", "f->g", "g-~>h", "h~>i some text", "h~->j"
		]
	}

Sharp lines
===========

.. pywave:: jsonml

	{ "signal": [
		{ "name": "A", "wave": "01..0..",  "node": ".a..e.." },
		{ "name": "B", "wave": "0.1..0.",  "node": "..b..d.", "phase":0.5 },
		{ "name": "C", "wave": "0..1..0",  "node": "...c..f" },
		{                              "node": "...g..h" }
	],
	"edge": [
		"b-|a t1", "a-|c t2", "b-|-c t3", "c-|->e t4", "e-|>f more text",
		"e|->d t6", "c-g", "f-h", "g<->h 3 ms"
	]}

==================
Step 10. From file
==================

.. pywave:: annotation.yaml

===============
Step 11. Figure
===============

.. pywave:: wavetest.json
	:caption: Figure caption
	:name: examplefig

========
Register
========

.. pywave:: jsonml-reg

  { "reg": [
    { "name": "IPO",   "bits": 8, "attr": "RO" },
    {                  "bits": 7 },
    { "name": "BRK",   "bits": 5, "attr": "RW", "type": 3 },
    { "name": "CPK",   "bits": 1 },
    { "name": "Clear", "bits": 3 },
    { "bits": 8 }
  ]}

