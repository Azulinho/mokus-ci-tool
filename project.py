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
    with open('gitlab-ci.yml', 'w') as f:
        gitlab_ci_job_config = _render_template(template, context)
        f.write(gitlab_ci_job_config)


def _build_docker_image(project_name):
    subprocess.call(
        [ 'docker' , 'build', '-t', project_name ]
    )


# public methods

def new(project_name, template, git_url):
    _create_gitlab_ci_job_config(project_name, template, git_url)
    #create_skeleton(template) # generates local skeleton for type of app


def build(project_name, template, git_url):
    # run the build steps locally for 'template'
    # do we need this ?
    # should we just use the template???
    # only reasone we would need a 'build' option is to support local builds
    # but that will require us to update this code when 'hacking' around.

    if template == 'marathon-docker-app':
        _build_docker_image(project_name)





