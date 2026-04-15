import subprocess


def run_behave_tests():
    cmd = [
        'behavex',
        '--parallel-processes', '5',
        '--parallel-scheme', 'scenario',
        '-o', 'behave-results'
    ]

    print('\n>>> Running tests')
    subprocess.run(cmd)


if __name__ == '__main__':
    run_behave_tests()
