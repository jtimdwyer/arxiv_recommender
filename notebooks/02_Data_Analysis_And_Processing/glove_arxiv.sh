#!/bin/bash
set -e

# This is where the GloVe binaries live
BUILDDIR=../../../GloVe/build

# These are the files we'll actually store out
CORPUS=../../vectors/arxiv_corpus.txt
VOCAB_FILE=../../vectors/GloVe_scratch_files/vocab_count.txt
COOCCURRENCE_FILE=../../vectors/GloVe_scratch_files/cooccurrence.bin
COOCCURRENCE_SHUF_FILE=../../vectors/GloVe_scratch_files/cooccurrence.shuf.bin
SAVE_FILE=../../vectors/GloVe_scratch_files/vectors


# Options for the various GloVe programs
VERBOSE=2
MEMORY=20
VOCAB_MIN_COUNT=100
VECTOR_SIZE=300
MAX_ITER=300
WINDOW_SIZE=15
BINARY=0
NUM_THREADS=8

$BUILDDIR/vocab_count -min-count $VOCAB_MIN_COUNT -verbose $VERBOSE < $CORPUS > $VOCAB_FILE

$BUILDDIR/cooccur -memory $MEMORY -vocab-file $VOCAB_FILE -verbose $VERBOSE -window-size $WINDOW_SIZE < $CORPUS > $COOCCURRENCE_FILE

$BUILDDIR/shuffle -memory $MEMORY -verbose $VERBOSE < $COOCCURRENCE_FILE > $COOCCURRENCE_SHUF_FILE

$BUILDDIR/glove -save-file $SAVE_FILE -threads $NUM_THREADS -input-file $COOCCURRENCE_SHUF_FILE -iter $MAX_ITER -vector-size $VECTOR_SIZE -binary $BINARY -vocab-file $VOCAB_FILE -verbose $VERBOSE