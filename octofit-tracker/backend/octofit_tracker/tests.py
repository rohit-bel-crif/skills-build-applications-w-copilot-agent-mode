from django.test import TestCase
from .models import Team, Activity, Leaderboard, Workout

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user_email='test@example.com', team='Test Team', type='Run', duration=30)
        self.assertEqual(str(activity), 'test@example.com - Run')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(team='Test Team', points=100)
        self.assertEqual(str(leaderboard), 'Test Team: 100')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Push Ups', difficulty='Easy')
        self.assertEqual(str(workout), 'Push Ups (Easy)')
