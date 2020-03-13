import time
import multiprocessing

from tasks import get_word_counts


PROCESSES = multiprocessing.cpu_count() - 1

def run():
    print(f'Running with {PROCESSES} processes!')
    start = time.time()
    with multiprocessing.pool(PROCESSES) as p:
        p.map_async(get_word_counts, [
            'pride-and-prejudice.txt',
            'heart-of-darkness.txt',
            'frankenstein.txt',
            'dracula.txt'
        ])
        p.close()
        p.join()
    print(f'Time taken {')