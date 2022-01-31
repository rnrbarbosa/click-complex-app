import nox

@nox.session
def tests(session):
    session.install('pytest','click')
    # Install in editable mode.
    session.install('-e', '.', '--no-deps')
    session.run('pytest')

