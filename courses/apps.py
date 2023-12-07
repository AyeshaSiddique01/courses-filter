"""
courses Django application initialization.
"""

from django.apps import AppConfig
from edx_django_utils.plugins.constants import PluginURLs
from openedx.core.djangoapps.plugins.constants import ProjectType

class CoursesConfig(AppConfig):
    """
    Configuration for the courses Django application.
    """

    name = 'courses'
    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                PluginURLs.NAMESPACE: 'courses',
                PluginURLs.REGEX: r'^api/courses/',
                PluginURLs.RELATIVE_PATH: 'urls',
            }
        }
    }
