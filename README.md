# Call Me Maybe
> Social Engineering Attack Suite for the Telephone Network (integrated with Plivo).

Disclaimer 1, this tool is only for use with numbers you are authorised to use. 

Disclaimer 2, this is nothing brilliant, it's really a tool to interact with the Plivo API with a certain goal...

Disclaimer 3, this code is bad. I know.

The initial features this tool allows are: Spoofing Phone Calls, Spoofing SMS. Soon: Brute Force Dialling of Phone Number Ranges (to detect valid phone company numbers/extensions and record audio)

> There are two versions of the tool, neither written well (IANAD - I am not a dev)
> There is a ruby version for cli, and a cut-down python version that runs a web interface and supports the spoofing functions only (ideal for mobile access)

![](screenshot.jpg)

## Requirements

Public IP Address

Ruby >= 2.0

Plivo >= 4.0.0

(gems as listed below)

## Installation

Required gems

```sh
gem install require_all
gem install tty-prompt
gem install builder
gem install rubygems
gem install plivo
gem install net
```

## Plivo API:

```sh
Add your Plivo API authentication to: ./config/config.rb
AUTH_ID = "<yourIDhere>"
AUTH_TOKEN = "<yourTokenhere>"
```

## Launching 

```sh
ruby main.rb
```

## Roadmap

* 0.0.1
    * Work in progress (spoofing modules built, but brute dialler not done.)
