import os
import subprocess
from jinja2 import Environment, FileSystemLoader
from jinja2 import Template


# private methods

PATH = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False
)

def _render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def _create_gitlab_ci_job_config(project_name, template, git_url):
    # grab the template for type 'template'
    # and populate it with 'project_name' and 'git_url'
    context = {
        'project_name': project_name,
        'git_url': git_url,
    }
    with open('.gitlab-ci.yml', 'w') as f:
        gitlab_ci_job_config = _render_template(
            "%s.gitlab.ci.jinja2" % template, context
        )
        f.write(gitlab_ci_job_config)

def _create_makefile(project_name, template, git_url):
    # grab the template for type 'template'
    # and populate it with 'project_name' and 'git_url'
    context = {
        'project_name': project_name,
        'git_url': git_url,
    }
    with open('Makefile', 'w') as f:
        makefile = _render_template(
            "%s.makefile.jinja2" % template, context
        )
        f.write(makefile)


# public methods

def new(project_name, template, git_url):
    _create_gitlab_ci_job_config(project_name, template, git_url)
    _create_makefile(project_name, template, git_url)
    #create_skeleton(template) # generates local skeleton for type of app

