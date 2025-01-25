'''###########################################################################
Command Line Interface
Author: Dolapo Ajayi
###########################################################################'''

import argparse

class cli_obj():

    def __init__(self, sys_args):
        parser = argparse.ArgumentParser(description='')

        parser.add_argument(
            '-b', '--job_board', required = True, 
            help = 'Provide a job board (indeed/linkedin/zip_recruiter/glassdoor/google).\n' 
            'You can also provide a comma separated list of job boards e.g. "indeed,linkedin".')
        parser.add_argument(
            '-j', '--job_title', required = True,
            help = 'Provide a Job title e.g. "bioinformatician".')
        parser.add_argument(
            '-c', '--city', required = True, 
            help = 'Enter the city of the job e.g. "Barcelona"')
        parser.add_argument(
            '-n', '--nation', required = True, 
            help = 'Enter the nation of the job e.g. "Spain"')
        self.args = parser.parse_args(sys_args)
