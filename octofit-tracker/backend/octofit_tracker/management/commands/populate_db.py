from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Create users
        User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel')
        User.objects.create(email='captain@marvel.com', name='Captain America', team='marvel')
        User.objects.create(email='batman@dc.com', name='Batman', team='dc')
        User.objects.create(email='superman@dc.com', name='Superman', team='dc')

        # Create activities
        Activity.objects.create(user='ironman@marvel.com', activity_type='run', duration=30, date='2026-02-16')
        Activity.objects.create(user='batman@dc.com', activity_type='cycle', duration=45, date='2026-02-15')

        # Create workouts
        Workout.objects.create(name='Pushups', description='Upper body', suggested_for='marvel')
        Workout.objects.create(name='Squats', description='Lower body', suggested_for='dc')

        # Create leaderboard
        Leaderboard.objects.create(team='marvel', points=200, rank=1)
        Leaderboard.objects.create(team='dc', points=180, rank=2)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
