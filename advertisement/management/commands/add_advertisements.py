import random

from django.core.management import BaseCommand


class Command(BaseCommand):

    help = "Fill db with N advertisements"

    def add_arguments(self, parser):
        parser.add_argument('-n', type=int, help="Сколько объявлений создать")

    def handle(self, *args, **options):
        if options['n']:
            from advertisement.models import Advertisement, AdvertisementType, AdvertisementStatus, Region
            number_of_regions = Region.objects.count()
            number_of_types = AdvertisementType.objects.count()
            status_to_add = AdvertisementStatus.objects.filter(name="Актуально").get()
            total = options["n"]
            for number in range(total):
                try:
                    random_region_count = random.randrange(1, number_of_regions+1)
                    random_region_ids = set()
                    random_type = AdvertisementType.objects.filter(id=random.randrange(1, number_of_types+1)).get()
                    for index in range(0, random_region_count):
                        random_region_ids.add(random.randrange(1, number_of_regions+1))
                    adv = Advertisement(title=f"Название{number}", description=f"Описание{number}",
                                        price=number, status=status_to_add,
                                        type=random_type)
                    adv.save()
                    for random_id in random_region_ids:
                        adv.region.add(Region.objects.filter(id=random_id).get())

                    adv.save()
                except Exception:
                    pass
