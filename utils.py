#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Copyright (C) 2017 Alpha Griffin

import os
import re
import time
import numpy as np
import ag.logging as log
import collections


__author__ = "Eric Petersen @Ruckusist"
__copyright__ = "Copyright 2017, The Alpha Griffin Project"
__credits__ = ["Eric Petersen", "Shawn Wilson", "@alphagriffin"]
__license__ = "***"
__version__ = "0.0.1"
__maintainer__ = "Eric Petersen"
__email__ = "ruckusist@alphagriffin.com"
__status__ = "Alpha"


class DataReader(object):
    """Parse and tokenize text documents."""
    def __init__(self, options, idx2word, word2idx):
        self.special_symbols()
        self.options = options
        self.idx2word = idx2word
        self.word2idx = word2idx
        self._buckets = [(5, 10), (10, 15), (20, 25), (40, 50)]

    def special_symbols(self):
        # Special vocabulary symbols - we always put them at the start.
        self._PAD = "_PAD"
        self._GO = "_GO"
        self._EOS = "_EOS"
        self._UNK = "_UNK"
        self._START_VOCAB = [self._PAD, self._GO, self._EOS, self._UNK]

        self.PAD_ID = 0
        self.GO_ID = 1
        self.EOS_ID = 2
        self.UNK_ID = 3

        # Regular expressions used to tokenize.
        self._WORD_SPLIT = re.compile("([.,!?\"':;)<>(])")
        self._DIGIT_RE = re.compile("\d")

    def basic_tokenizer(self, sentence):
        """Very basic tokenizer: split the sentence into a list of tokens."""
        words = []
        for space_separated_fragment in sentence.strip().split():
            word = re.split(self._WORD_SPLIT, space_separated_fragment)
            # word = re.sub(self._DIGIT_RE, "0", word)
            words.extend(word)
        return [w for w in words if w]

    def read_data(self, fname=None, normalize_digits=True):
        """Create numpy representation of text from path."""
        if fname is None:
            fname = "text/test.txt"
        log.info("Processing text at path: {}".format(fname))
        if not os.path.isfile(fname):
            log.warn("{} is an invalid path".format(fname))
            return False
        class sample_text: pass
        # starting
        vocab = {}
        with open(fname) as f:
            counter = 0
            for line in f:
                counter += 1
                if counter % 100000 == 0:
                    print("Processing line #{}...".format(counter))
                # print(line)
                tokens = self.basic_tokenizer(line)
                for w in tokens:
                    word = re.sub(self._DIGIT_RE, "0", w) if normalize_digits else w
                    if word in vocab:
                        vocab[word] += 1
                    else:
                        vocab[word] = 1
        # finishing
        vocab_list = self._START_VOCAB + sorted(vocab, key=vocab.get, reverse=True)
        log.info('>> Full Vocabulary Size : {}'.format(len(vocab_list)))

        # add words to database
        for index, word in enumerate(vocab_list):
            log.debug("adding word \"{}\" to database @ {}".format(word, index))
            self.idx2word.write_data(str(index), str(word))
            self.word2idx.write_data(str(word), str(index))
            # how much time does this add???
            read_back = int(self.word2idx.read_data(str(word)))
            assert index == read_back

        # sanity check
        if False:
            encoded_sample = self.encode_line(line)
            print("Sample Encoded Line:\n{} == {}".format(line, encoded_sample))
            decoded_sample = self.decode_line(encoded_sample)
            print("Sample Decoded line: {}".format(decoded_sample))

        # fin
        log.info("File Loaded successfully.")
        return True

    def encode_line(self, data):
        """Use redis for managing a dynamic words library."""
        log.info("Accessing redis for text management.")
        words = self.basic_tokenizer(data)
        encoded_line = []
        for w in words:
            id_for_word = self.word2idx.read_data(w)
            encoded_line.append(id_for_word)
        return encoded_line

    def decode_line(self, data):
        """Use redis for managing a dynamic words library."""
        log.info("Accessing redis for text management.")
        decoded_line = ""
        for w in data:
            word_for_id = self.idx2word.read_data(str(w))
            decoded_line += word_for_id + " "
        return decoded_line

    def make_buckets(self):
        """Still not working"""
        # data struct for passing back to program
        data_set = [[] for _ in self._buckets]
        # get the datafiles for processing.
        for f in os.listdir(os.path.join(os.getcwd(), self.options.input_text_path)):
            print(f)


        return "stuff"
