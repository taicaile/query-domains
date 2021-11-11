"""query domains"""
import argparse
import itertools
import logging
import string
import subprocess
from datetime import date


def logger_init(domain: str):
    """logger initialize"""
    # remove handlers
    logger = logging.getLogger()
    while logger.hasHandlers():
        logger.removeHandler(logger.handlers[0])
    # add handlers
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(message)s",
        filename=str(date.today()) + "_" + domain + ".log",
        filemode="w",
    )

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(asctime)s %(name)s [%(levelname)-5s]: %(message)s", datefmt="%H:%M:%S"
    )
    console.setFormatter(formatter)
    logging.getLogger("").addHandler(console)


def whois(domain):
    """check if a domain is registered"""
    whois_cmd = f'whois {domain} | grep "Domain Name"'
    proc = subprocess.run(
        whois_cmd, shell=True, capture_output=True, text=True, check=False
    )
    return proc.returncode == 0


def query_domains(domain: str):
    """query domains for all matchings"""
    found = 0
    unknows = domain.count("?")
    total = len(string.ascii_lowercase) ** unknows
    domain_fmt = domain.replace("?", "%s")
    for values in itertools.combinations_with_replacement(
        string.ascii_lowercase, unknows
    ):
        # pytlint: disable=logging-not-lazy
        new_domain = domain_fmt % values
        if not whois(new_domain):
            found += 1
            logging.info("%s/%s %s has not registered yet.", found, total, new_domain)
        else:
            logging.info("%s/%s %s is registered.", found, total, new_domain)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--domains", nargs="+", required=True, help="e.g. --domains ???.com"
    )

    args = parser.parse_args()

    for d in args.domains:
        logger_init(d)
        query_domains(d)
