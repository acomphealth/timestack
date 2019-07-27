import setuptools


def main():
	with open("README.md", "r") as fh:
		long_description = fh.read()
		setuptools.setup(
			name='timestack',
			version='0.1',
			author="Association for Computational Health",
			author_email="wade.schulz@yale.edu",
			description="A Python library for time manipulation oriented to the OMOP Clinical data standard",
			long_description=long_description,
			long_description_content_type="text/markdown",
			url="https://github.com/acomphealth/timestack",
			packages=setuptools.find_packages(),
			classifiers=[
				"Programming Language :: Python :: 3",
				"License :: OSI Approved :: Apache License v2",
				"Operating System :: OS Independent",
			]
		)


if __name__ == "__main__":
	main()
