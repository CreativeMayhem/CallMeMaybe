# Call Me Maybe
> Social Engineering Attack Suite for the Telephone Network (integrated with Plivo).

[![NPM Version][npm-image]][npm-url]
[![Build Status][travis-image]][travis-url]
[![Downloads Stats][npm-downloads]][npm-url]

The initial features this tool allows is: Spoofing Phone Calls, Spoofing SMS, Brute Force Dialling of Phone Number Ranges (to detect valid phone company numbers/extensions and record audio)

![](screenshot.jpg)

## Requirements

Ruby >= 2.0
Plivo >= 4.0.0
(gems as listed below)

## Installation

Required gems

```sh
gem instal require_all
gem install tty-prompt
gem install builder
gem install rubygems
gem install plivo
gem install net
```

Plivo API:

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

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki