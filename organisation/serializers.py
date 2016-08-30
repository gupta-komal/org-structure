from django.contrib.auth.models import User
from rest_framework import serializers
from assignment import settings
from organisation.models import Repo, Team, Organisation


class RepoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Repo
        fields = ('repo_name',)


class OrgMiniSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organisation
        fields = ('name',)


class TeamOrgSerializer(serializers.ModelSerializer):
    team_repo = RepoSerializer(many=True, read_only=True)
    org = OrgMiniSerializer(read_only=True)

    class Meta:
        model = Team
        fields = ('name', 'team_repo', 'org')


class TeamMiniSerializer(serializers.ModelSerializer):
    team_repo = RepoSerializer(many=True, read_only=True)
    team_set = TeamOrgSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ('name', 'team_repo', 'team_set')


class TeamSerializer(serializers.ModelSerializer):
    team_repo = RepoSerializer(many=True, read_only=True)
    team_set = TeamMiniSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        field = ('team_repo', 'team_set', 'name')

    def __init__(self, *args, **kwargs):
        for field in settings.TEAM_JOSN_REMOVE:
            self.fields.fields.pop(field)
        super(TeamSerializer, self).__init__(*args, **kwargs)


class OrganisationSerializer(serializers.ModelSerializer):
    org_team = TeamSerializer(many=True, read_only=True)

    class Meta:
        model = Organisation
        field = ('name', 'org_team')

    def __init__(self, *args, **kwargs):
        self.fields.fields.pop('id')
        super(OrganisationSerializer, self).__init__(*args, **kwargs)


class UserSerializer(serializers.ModelSerializer):
    user_team = TeamOrgSerializer(many=True, read_only=True)

    class Meta:
        model = User
        field = ('email', 'user_team')

    def __init__(self, *args, **kwargs):
        for field in settings.USER_JSON_REMOVE:
            self.fields.fields.pop(field)
        super(UserSerializer, self).__init__(*args, **kwargs)
