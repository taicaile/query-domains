# README

This script is used to query `whois` information for a batch of domains.

To run this script,

```bash
# to check any available domain with `???.cc` pattern
python query.py --domain-name ???.cc
```

Make sure `whois` is installed,

```bash
sudo apt install whois
```

## API

- ovh (<https://github.com/alexisvisco/ovh-domain-api>)

- check per tls
  <https://github.com/twiny/domain>

- <https://github.com/baibhavanand/DAC/blob/main/dac>

## TODO

- [x] add `start-from` option

- [ ] merge all existing APIs.
