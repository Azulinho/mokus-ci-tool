import click
import project

@click.group()
def cli():
    pass

@click.command()
@click.option('--template')
@click.option('--project-name')
@click.option('--git-url')
def new(project_name, template, git_url):
    project.new(project_name, template, git_url)

cli.add_command(new)

if __name__ == '__main__':
    cli()