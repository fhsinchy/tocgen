# Table of Content (toc) Generator (gen)

Creating clickable table of content for my handbooks manually was a hectic task. So I created this Python script that does the work for me.

## Requirements

* Python 3

## Installation

```shell
pip install git+https://github.com/fhsinchy/tocgen.git#egg=tocgen
pip freeze
```

Output &ndash;

```shell
tocgen==1.0.0
```

## Usage

Once you have installed the package it should be available everywhere in your system. The generic command for executing this script is

```shell
tocgen <url to your article preview>
```

The script will create a new markdown file for you that you can copy and paste into your freeCodeCamp article as the table of content. Keep in mind, the script only considers `h2` and `h3` element when generating the table of content. Since I never go deeper than one layer of nesting in my table of contents, I didn't bother accounting for the other header types.