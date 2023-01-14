from companies.amazon import AmazonApiJobScrapper
from companies.atlassian import AtlassianApiJobScrapper
from companies.blinkit import BlinkItBSJobScrapper
from companies.cashfree import CashFreeBSJobScrapper
from companies.coursera import CourseraBSJobScrapper
from companies.cred import CREDApiJobScrapper
from companies.drivetrain import DrivetrainBSJobScrapper
from companies.epifi import EpiFiBSJobScrapper
from companies.frontrow import FrontRowApiJobScrapper
from companies.grab import GrabBSJobScrapper
from companies.groww import GrowwApiJobScrapper
from companies.jumbotail import JumboTailBSJobScrapper
from companies.lenskart import LensKartBSJobScrapper
from companies.nutanix import NutanixApiJobScrapper
from companies.paytm import PaytmBSJobScrapper
from companies.pharmeasy import PharmEasyApiJobScrapper
from companies.phonepe import PhonePeApiJobScrapper
from companies.shiprocket import ShipRocketBSJobScrapper
from companies.spinny import SpinnyBSJobScrapper
from companies.uber import UberApiJobScrapper
from companies.upgrad import UpGradApiJobScrapper
from companies.zeta import ZetaApiJobScrapper

SCRAPPERS = [
    CREDApiJobScrapper(),
    AtlassianApiJobScrapper(),
    AmazonApiJobScrapper(),
    DrivetrainBSJobScrapper(),
    UberApiJobScrapper(),
    PhonePeApiJobScrapper(),
    ZetaApiJobScrapper(),
    NutanixApiJobScrapper(),
    PaytmBSJobScrapper(),
    CashFreeBSJobScrapper(),
    CourseraBSJobScrapper(),
    JumboTailBSJobScrapper(),
    GrowwApiJobScrapper(),
    UpGradApiJobScrapper(),
    GrabBSJobScrapper(),
    PharmEasyApiJobScrapper(),
    ShipRocketBSJobScrapper(),
    FrontRowApiJobScrapper(),
    SpinnyBSJobScrapper(),
    BlinkItBSJobScrapper(),
    EpiFiBSJobScrapper(),
    LensKartBSJobScrapper()
]

COMPANY_LOGO_MAP = {scrapper.get_name(): scrapper.get_image_url() for scrapper in SCRAPPERS}
