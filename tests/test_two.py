import two


def test_known_good():
    reports = [
        [
            7,
            6,
            4,
            2,
            1,
        ],
        [
            1,
            2,
            7,
            8,
            9,
        ],
        [
            9,
            7,
            6,
            2,
            1,
        ],
        [
            1,
            3,
            2,
            4,
            5,
        ],
        [
            8,
            6,
            4,
            4,
            1,
        ],
        [
            1,
            3,
            6,
            7,
            9,
        ],
    ]
    safe_reports = 0
    for report in reports:
        if two.evaluate_report(report):
            safe_reports += 1
    assert safe_reports == 2