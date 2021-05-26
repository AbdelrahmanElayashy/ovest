"""Main module."""

from ovest.acceleration import run as accer
from ovest.alert import run as alert
from ovest.alert.gbs import run as gbs
from ovest.alert.gsm import run as gsm
from threading import Thread


def main():
