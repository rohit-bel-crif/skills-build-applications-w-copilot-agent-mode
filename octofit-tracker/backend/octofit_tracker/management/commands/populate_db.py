
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout
import pymongo

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        users = [
            {'email': 'ironman@marvel.com', 'username': 'Iron Man', 'team': 'Marvel'},
            {'email': 'captain@marvel.com', 'username': 'Captain America', 'team': 'Marvel'},
            {'email': 'spiderman@marvel.com', 'username': 'Spider-Man', 'team': 'Marvel'},
            {'email': 'batman@dc.com', 'username': 'Batman', 'team': 'DC'},
            {'email': 'superman@dc.com', 'username': 'Superman', 'team': 'DC'},
            {'email': 'wonderwoman@dc.com', 'username': 'Wonder Woman', 'team': 'DC'},
        ]
        for u in users:
            User.objects.create_user(email=u['email'], username=u['username'], password='password123')

        Activity.objects.create(user_email='ironman@marvel.com', team='Marvel', type='Running', duration=30)
        Activity.objects.create(user_email='batman@dc.com', team='DC', type='Cycling', duration=45)
        Activity.objects.create(user_email='spiderman@marvel.com', team='Marvel', type='Swimming', duration=25)
        Activity.objects.create(user_email='superman@dc.com', team='DC', type='Running', duration=60)

        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=120)

        Workout.objects.create(name='Push Ups', difficulty='Easy')
        Workout.objects.create(name='Pull Ups', difficulty='Medium')
        Workout.objects.create(name='Squats', difficulty='Easy')
        Workout.objects.create(name='Deadlift', difficulty='Hard')

        # Create unique index on email for users collection using pymongo
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client['octofit_db']
        db['users'].create_index('email', unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
