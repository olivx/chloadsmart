from django.core.management.base import BaseCommand
from django.contrib.gis.geos import fromstr
from django.conf import settings
import csv
import pathlib
from core.models import Cargo, Trucks

class Command(BaseCommand):
    help = 'Send test emails'

    def __init__(self):
        self._path =  pathlib.Path(settings.BASE_DIR).joinpath("data")

    def handle(self, *args, **options):

        cargos = Cargo.objects.values_list("product",flat=True)
        trucks = Trucks.objects.values_list("truck",flat=True)

        self.add_cargos(cargos)
        self.add_trucks(trucks)

    def add_trucks(self, trucks):
        """ init database with  truck  information from csv """
        with open(self._path.joinpath('trucks.csv')) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row.get('truck') in trucks:
                    print(f"truck find in database {row.get('truck')}")

                else:
                    point = fromstr(f"POINT({row.get('lat')} {row.get('lng')})", srid=4326)
                    cargo =  Trucks(
                        truck=row.get('truck'),
                        city=row.get('city'),
                        state=row.get('state'),
                        point=point,
                    )
                    cargo.save()

            print("Trucks imported successful")

    def add_cargos(self, cargos):
        """ init database with  cargos  information from csv """
        with open(self._path.joinpath('cargos.csv')) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row.get('product') in cargos:
                    print(f"product find in database {row.get('product')}")

                else:
                    origin_point = fromstr(f"POINT({row.get('origin_lat')} {row.get('origin_lng')})", srid=4326)
                    destination_point = fromstr(f"POINT({row.get('destination_lat')} {row.get('destination_lng')})", srid=4326)
                    cargo =  Cargo(
                        product=row.get('product'),
                        origin_city=row.get('origin_city'),
                        origin_state=row.get('origin_state'),
                        destination_city=row.get('destination_city'),
                        destination_state=row.get('destination_state'),
                        origin_point=origin_point,
                        destination_point=destination_point,
                    )
                    cargo.save()

            print("Cargos imported successful")