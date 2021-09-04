#!/bin/bash

echo -n "Enter a site's domain name (i.e. '{{cookiecutter.domain_name}}'): "
read site
whois $site
host -a $site
