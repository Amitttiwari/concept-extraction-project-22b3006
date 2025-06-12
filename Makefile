run:
	python main.py --subject=$(subject)

run-all:
	python main.py --subject=ancient_history
	python main.py --subject=economics
	python main.py --subject=math
	python main.py --subject=physics

▶️ Usage
To run for one subject:

make run subject=ancient_history

To run for all subjects:

make run-all
