FILE_PATH = "scores.txt"
OUTPUT_PATH = "log.txt"

BAD_SCORE_VALUE_ERROR = "Bad score value for {}, ignored."
MEAN_SCORE_OUTPUT = "The class average is {:g} for {} student{}."

class Logger():

    _log_file = None

    def __init__(self, file_path):
        try:
            self._log_file = open(file_path, "w+")
        except IOError as error:
            print(error)

    def log(self, string):
        print(string)
        if self._log_file != None:
            self._log_file.write(string + "\n")

    def __del__(self):
        if self._log_file != None:
            self._log_file.close()
    
logger = Logger(OUTPUT_PATH)

def get_data_from_file(file_path):
    f = open(file_path, "r")
    data = f.read()
    f.close()
    return data

def parse_data(raw_data):

    scores = []

    line_delimiter = "\n"
    item_delimiter = " "
    
    lines = raw_data.split(line_delimiter)

    for line in lines:
        chunks = line.split(item_delimiter)

        while "" in chunks:
            chunks.remove("")

        if len(chunks) == 0:
            continue

        try:
            name = chunks[0]
            score = int(chunks[1])
        except (ValueError, IndexError):
            logger.log(BAD_SCORE_VALUE_ERROR.format(name))
            continue

        scores.append(score)

    return scores

def task1():
    try:
        file_data = get_data_from_file(FILE_PATH)
    except IOError as error:
        print(error)
        return

    sanitized_scores = parse_data(file_data)
    scores_count = len(sanitized_scores)
    if scores_count != 0:
        mean = sum(sanitized_scores) / scores_count
    else:
        mean = 0

    logger.log(MEAN_SCORE_OUTPUT.format(mean, scores_count, "s" if scores_count != 1 else ""))

task1()
