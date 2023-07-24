#!/usr/bin/python3

import sys
import os

from typing import Tuple

# TODO: Explain what you did

# the location in save file that corresponds to the size of data path
DATA_SIZE_LOC = 0x2

CAM_DIFFICULTY_LOC = 0x65
BATTLE_DIFFICULTY_LOC = 0x87

def get_difficulty_rep(difficulty_number: int) -> str:
        if(difficulty_number == 0):
            return "easy"
        elif(difficulty_number == 1):
            return "medium"
        elif(difficulty_number == 2):
            return "hard"
        elif(difficulty_number == 3):
            return "very hard"
        else:
            return "something went wrong"

# path: path to the save file
# result will be returned as a tuple.
# first element is campaign's difficulty and the second is battle's difficulty
def get_all_difficulty(path: str) -> Tuple[int]:
    with open(path, 'rb') as save_file:
        # reading the data path size
        save_file.seek(DATA_SIZE_LOC)
        # each character is 2 bytes so we multiply the size by 2
        data_size = int.from_bytes(save_file.read(1))*2

        # the difiiculty integer is 4 bytes, so we read 4 bytes
        save_file.seek(CAM_DIFFICULTY_LOC + data_size)
        cam_difficulty = int.from_bytes(save_file.read(4), "little")

        # the difiiculty integer is 4 bytes, so we read 4 bytes
        save_file.seek(BATTLE_DIFFICULTY_LOC + data_size)
        battle_difficulty = int.from_bytes(save_file.read(4), "little")

        result = (cam_difficulty, battle_difficulty)
        return result

def print_all_difficulty(path: str):
    difficulties = get_all_difficulty(path)
    cam_difficulty = get_difficulty_rep(difficulties[0])
    battle_difficulty = get_difficulty_rep(difficulties[1])
    print(f"Campaign's difficulty is {cam_difficulty}")
    print(f"Battle's difficulty is {battle_difficulty}")

def return_help():
    help = """
    A python script to determine the difficulty of a medieval save file, both campaign and battle.
    Usage: medieval_diff.py [file]
    """
    return help

if __name__ == "__main__":
    if(len(sys.argv) == 1):
        print(return_help())
    elif(len(sys.argv) == 2):
        save_file_path = sys.argv[1]
        if(os.path.isfile(save_file_path)):
            print_all_difficulty(save_file_path)
        else:
            print("No such file! Check if you entered the path correctly")