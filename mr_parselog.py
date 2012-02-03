import sys
from mrjob.protocol import JSONValueProtocol
from mrjob.job import MRJob
from term_tools import get_terms

class MRParseLog(MRJob):
    DEFAULT_INPUT_PROTOCOL = 'raw_value'
    DEFAULT_OUTPUT_PROTOCOL = 'raw_value'

    def mapper(self, _, line):
        for term in get_terms(email['text']):
            yield {'term': term, 'sender': email['sender']}, 1

    def reducer(self, term_sender, howmany):
        yield None, {'term_sender': term_sender, 'count': sum(howmany)}

if __name__ == '__main__':
        MRWCBySender.run()
