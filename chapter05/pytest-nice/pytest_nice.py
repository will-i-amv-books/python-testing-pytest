def pytest_addoption(parser):
    """Turn nice features on with --nice option."""
    group = parser.getgroup('nice')
    group.addoption(
        "--nice",
        action="store_true",
        help="nice: turn failures into opportunities"
    )


def pytest_report_header(config):
    """Thank tester for running tests."""
    if config.getoption(name='nice'):
        return "Thanks for running the tests."


def pytest_report_teststatus(report, config):
    """Turn failures into opportunities."""
    if report.when == 'call':
        if report.failed and config.getoption(name='nice'):            
            return (report.outcome, 'O', 'OPPORTUNITY for improvement')
