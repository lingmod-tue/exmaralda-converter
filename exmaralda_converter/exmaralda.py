""" Collection of classes required to represent a conversation transcript in Exmaralda format

created: by Zarah Weiss, October 2017
Modificaion history:
- Zarah Weiss, August 2019: introduced proper comments
- Zarah Weiss, March 2020: allow to load exmaralda transcript into python
TODO Careful! Made changes to Tier, now speakers are optional and strings in tiers rather than mandatory speaker objects
TODO make this compatible with transcript.py
"""
__author__ = 'zweiss'

import os
import xml.etree.ElementTree as ET


class Speaker:
    """Represents an individual speaker represented in a conversation transcript.

    Attributes
    ----------
    speaker_id: str
        the unique id of a speaker (default is empty string)
    abbreviation: str
        the abbreviation used to match a turn in the transcript to a speaker (default is empty string)
    sex: str
        the gender of the speaker (default is empty string)
    languages_used: str or [str]
        list of languages spoken by the speaker in the transcript (default is empty string)
    l1: str or [str]
        first language(s) of the speaker (default is empty string)
    l2: str or [str]
        second language(s) of the speaker (default is empty string)
    ud_speaker_information: str
        additional(?) speaker information (default is empty string)
    comment: str
        comments on the speaker (default is empty string)

    Methods
    -------
    add_l1(new_l1):
        Adds a first language to the list of first languages
    add_l2(new_l2):
        Adds a second language to the list of first languages to the list of L2(s)
    add_language_used(new_language_used):
        Adds a language used in the conversation by the speaker to the list of languages used
    pretty_print(indentation_level=0):
        Creates an indented xml representation of the object following Exmaralda standards
    """

    def __init__(self, speaker_id='', abbreviation='', sex='', languages_used='', l1='', l2='', ud_speaker_information='', comment=''):
        """
        :param speaker_id: the unique id of a speaker
        :type speaker_id: str (optional, defaults to '')
        :param abbreviation: the abbreviation used to match a turn in the transcript to a speaker
        :type abbreviation: str (optional, defaults to '')
        :param sex: the gender of the speaker
        :type sex: str (optional, defaults to '')
        :param languages_used: list of languages spoken by the speaker in the transcript
        :type languages_used: str or list of strings (optional, defaults to '')
        :param l1: first language(s) of the speaker
        :type l1: str or list of strings (optional, defaults to '')
        :param l2: str or [str], optional: second language(s) of the speaker
        :type l2: str or list of strings (optional, defaults to '')
        :param ud_speaker_information: TODO
        :type languages_used: str (optional, defaults to '')
        :param comment: comments on the speaker
        :type comment: str (optional, defaults to '')
        """

        self.speaker_id = speaker_id
        self.abbreviation = abbreviation
        self.sex = sex
        self.languages_used = [] if isinstance(languages_used, str) else languages_used
        self.l1 = [] if isinstance(l1, str) else l1
        self.l2 = [] if isinstance(l2, str) else l2
        self.ud_speaker_information = ud_speaker_information
        self.comment = comment

    # definition of built-in methods

    def __eq__(self, other):
        if not self.speaker_id == other.speaker_id:
            return False
        if not self.abbreviation== other.abbreviation:
            return False
        if not self.sex == other.sex:
            return False
        if not set(self.languages_used) == set(other.languages_used):
            return False
        if not set(self.l1) == set(other.l1):
            return False
        if not set(self.l2) == set(other.l2):
            return False
        if not self.ud_speaker_information == other.ud_speaker_information:
            return False
        if not self.comment== other.comment:
            return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return self.pretty_print(0)

    def __lt__(self, other):
        return self.speaker_id < other.speaker_id

    def __le__(self, other):
        return self.speaker_id <= other.speaker_id

    def __gt__(self, other):
        return self.speaker_id > other.speaker_id

    def __ge__(self, other):
        return self.speaker_id <= other.speaker_id

    # setter
    # TODO delete setter and getter, no one needs these

    def set_speaker_id(self, speaker_id):
        self.speaker_id = speaker_id

    def set_abbreviation(self, abbreviation):
        self.abbreviation = abbreviation

    def set_sex(self, sex):
        self.sex = sex

    def set_languages_used(self, languages_used):
        self.languages_used = languages_used

    def set_l1(self, l1):
        self.l1 = l1

    def set_l2(self, l2):
        self.l2 = l2

    def set_ud_speaker_information(self, ud_speaker_information):
        self.ud_speaker_information = ud_speaker_information

    def set_comment(self, comment):
        self.comment = comment

    # getter

    def get_speaker_id(self):
        return self.speaker_id

    def get_abbreviation(self):
        return self.abbreviation

    def get_sex(self):
        return self.sex

    def get_languages_used(self):
        return self.languages_used

    def get_l1(self):
        return self.l1

    def get_l2(self):
        return self.l2

    def get_ud_speaker_information(self):
        return self.ud_speaker_information

    def get_comment(self):
        return self.comment

    # additional methods

    def add_l1(self, new_l1):
        """ Adds a first language to the list of first languages

        :param new_l1: new language to be added to the list of L1(s)
        :type new_l1: str
        """

        self.l1.append(new_l1)

    def add_l2(self, new_l2):
        """ Adds a second language to the list of first languages to the list of L2(s)

        :param new_l2: new language to be added
        :type new_l2: str
        """

        self.l2.append(new_l2)

    def add_language_used(self, new_language_used):
        """ Adds a language used in the conversation by the speaker to the list of languages used

        :param new_language_used: new language to be added
        :type new_language_used: str
        """

        self.languages_used.append(new_language_used)

    # printing

    def pretty_print(self, indentation_level=0):
        """ Creates an indented xml representation of the object following Exmaralda standards

        :param indentation_level: current indentation level for printing within nested xml structure
        :type indentation_level: int (optional, defaults to 0)
        :return: indented xml representation of all speaker data
        :rtype: str
        """

        indent = '\t'*indentation_level
        rval = '{}<speaker id="{}">'.format(indent, self.speaker_id)
        rval += '{}{}\t<abbreviation>{}</abbreviation>{}'.format(os.linesep, indent, self.abbreviation, os.linesep)
        rval += '{}\t<sex value="{}"/>{}'.format(indent, self.sex, os.linesep)
        rval += '{}\t<languages-used>{}</languages-used>{}'.format(indent, ', '.join(self.languages_used), os.linesep)
        rval += '{}\t<l1>{}</l1>{}'.format(indent, ', '.join(self.l1), os.linesep)
        rval += '{}\t<l2>{}</l2>{}'.format(indent, ', '.join(self.l2), os.linesep)
        rval += '{}\t<ud-speaker-information>{}</ud-speaker-information>{}'.format(indent, self.ud_speaker_information, os.linesep)
        rval += '{}\t<comment>{}</comment>{}'.format(indent, self.comment, os.linesep)
        rval += '{}</speaker>'.format(indent)
        return rval


class Timepoint:
    """ Class representation of turn time points

    Attributes
    ----------
    running_id: int
        a running id for time points starting with 0
    time_id: int
        specific time point id assigned to a class instance based on the running id
    time_stamp: int, optional
        time stamp of turn
    type: str, optional
        beginning or end of conversation  # TODO figure out if this is true!

    Methods
    -------
    pretty_print(indentation_level=0):
        Creates an indented xml representation of the object following Exmaralda standards
    """

    running_id = 0

    def __init__(self, time_stamp=-1, type=''):
        """
        :param time_stamp: time stamp of turn
        :type time_stamp: int (optional, defaults to -1)
        :param type: beginning or end of conversation  # TODO figure out if this is true!
        :type type: str (optional, defaults to '')
        """

        self.time_stamp = time_stamp
        self.time_id = Timepoint.running_id
        Timepoint.running_id += 1
        self.type = type

    # definition of built-in methods

    def __del__(self):
        Timepoint.running_id -= 1

    def __str__(self):
        return self.pretty_print(0)

    def __eq__(self, other):
        return self.time_id == other.time_id and self.time_stamp == other.time_stamp

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.time_stamp < other.time_stamp

    def __le__(self, other):
        return self.time_stamp <= other.time_stamp

    def __gt__(self, other):
        return self.time_stamp > other.time_stamp

    def __ge__(self, other):
        return self.time_stamp >= other.time_stamp

    # setter
    # TODO delete setter and getter, no one needs these

    def set_type(self, type):
        self.type = type

    def set_time_id(self, time_id):
        self.time_id = time_id

    def set_time_stamp(self, time_stamp):
        self.time_stamp = time_stamp

    # getter

    def get_time_stamp(self):
        return self.time_stamp

    def get_time_id(self):
        return self.time_id

    def get_type(self):
        return self.type

    # printing

    def pretty_print(self, indentation_level=0):
        """ Creates an indented xml representation of the object following Exmaralda standards

        :param indentation_level: current indentation level for printing within nested xml structure
        :type indentation_level: int (optional, defaults to 0)
        :return: indented xml representation of the time point data
        :rtype: str
        """

        indent = '\t'*indentation_level
        rval = '{}<tli id="T{}"'.format(indent, self.get_time_id()) if self.time_stamp == -1 else '{}<tli id="T{}" time="{}"'.format(indent, self.get_time_id(), self.time_stamp)
        if len(self.type) == 0:
            return rval + '/>'
        return rval + ' type="{}"/>'.format(self.type)


class Event:
    """ Represents a contribution event in a conversation transcript, e.g. a spoken turn or a gesture

    Attributes
    ----------
    start: TODO
        start time of the event
    end: TODO
        end time of the event
    content: TODO
        event content (e.g., transcription of speech in a turn)

    Methods
    -------
    pretty_print(indentation_level=0):
        Creates an indented xml representation of the object following Exmaralda standards
    """

    def __init__(self, start, end, content=''):
        """
        :param start: start time of the event
        :type start: TODO
        :param end: end time of the event
        :type end: TODO
        :param content: event content (e.g., transcription of speech in a turn)
        :type content: TODO
        """

        self.start = start
        self.end = end
        self.content = content

    # definition of built-in methods

    def __str__(self):
        return self.pretty_print(0)

    # setter
    # TODO delete setter and getter, no one needs these

    def set_content(self, content):
        self.content = content

    # getter

    def get_start_id(self):
        return self.start.time_id

    def get_end_id(self):
        return self.end.time_id

    def get_content(self):
        return self.content

    # printing

    def pretty_print(self, indentation_level=0):
        """ Creates an indented xml representation of the object following Exmaralda standards

        :param indentation_level: current indentation level for printing within nested xml structure
        :type indentation_level: int (optional, defaults to 0)
        :return: indented xml representation of the event data
        :rtype: str
        """

        indent = '\t'*indentation_level
        return '{}<event start="T{}" end="T{}">{}</event>'.format(indent, self.get_start_id(), self.get_end_id(), self.content)


class Tier:
    """

    Attributes
    ----------


    Methods
    -------
    pretty_print(indentation_level=0):
        Creates an indented xml representation of the object following Exmaralda standards
    is_empty():
        Checks if the event list is empty
    add_event(e):
        Adds an event to the list of events
    """

    # TODO define parameters
    # TODO do not force tiers to have a speaker and allow tiers to have an id
    def __init__(self, id, speaker='', category='v', type='t', display_name=''):
        """
        :param speaker: speaker associated with this tear
        :type speaker: str
        :param category: TODO
        :type category: str (optional, defaults to 'v')
        :param type: TODO
        :type type: str (optional, defaults to 't')
        :param display_name: name to be displayed when printing
        :type display_name: str (optional, defaults to '')
        """

        self.id = id
        self.speaker = speaker
        self.category = category
        self.type = type
        self.display_name = display_name
        self.event_list = []

    # definition of built-in methods

    def __str__(self):
        return self.pretty_print(0)

    # setter
    # TODO delete setter and getter, no one needs these

    def set_speaker(self, s):
        self.speaker = s

    def set_id(self, id):
        self.id = id

    def set_category(self, cat):
        self.category = cat

    def set_type(self, type):
        self.type = type

    def set_display_name(self, name):
        self.display_name = name

    def set_event_list(self, elist):
        self.event_list = elist

    # getter

    def get_tier_id(self):
        return self.id

    def get_speaker(self):
        return self.speaker

    def get_category(self):
        return self.category

    def get_type(self):
        return self.type

    def get_display_name(self):
        return self.display_name

    def get_event_list(self):
        return self.event_list

    # printing

    def pretty_print(self, indentation_level=0):
        """ Creates an indented xml representation of the object following Exmaralda standards

        :param indentation_level: current indentation level for printing within nested xml structure
        :type indentation_level: int (optional, defaults to 0)
        :return: str: indented xml representation of the tier point data
        :rtype str
        """

        indent = '\t'*indentation_level
        rval = '{}<tier id="{}"{} category="{}" type="{}" display-name="{}">'.format(indent, self.id,
                                                                                   ' speaker="'+self.speaker+'"' if len(self.speaker)>0 else '',
                                                                                     self.category,
                                                                                     self.type,
                                                                                     self.display_name)
        if len(self.event_list) == 0:
            return rval + '</tier>'
        rval += '\n'+'\n'.join([e.pretty_print(indentation_level+1) for e in self.event_list])
        rval += '\n{}</tier>'.format(indent)
        return rval

    # additional methods

    def is_empty(self):
        """ Checks if the event list is empty

        :return: true if length of list equals 0
        :rtype: bool
        """

        return len(self.event_list) == 0

    def add_event(self, e):
        """ Adds an event to the list of events

        :param e: event to be added
        :type e: Event
        """

        self.event_list.append(e)


class ExmaraldaTranscript:
    """ Represents a full conversation transcript with multiple interlocutors in Exmaralda format

    Attributes
    ----------
    preface: str
        header line shared by all exmaralda transcripts specifying the version, encoding, and exmaralda copyright
    meta_information: dict
        dictionary including information on the project name, transcription name, referenced file url, ud meta
        information, comments, and transcription convention used
    speaker_table: dict
        dictionary listing all speakers participationg in the conversation
    timeline: list of Timepoint objects
        records the timeline of turns
    tiers: dict
        contains all conversational tiers of the transcript

    Methods
    -------
    add_speaker(speaker_id, abbreviation='', sex='', languages_used='', l1='', l2='', ud_speaker_information='', comment='', display_name=""):
        Adds a speaker who is contributing to the converstaion to the speaker table and tier dictionary
    overwrite_speaker(speaker_id, abbreviation='', sex='', languages_used='', l1='', l2='', ud_speaker_information='', comment=''):
        Overwrites a speaker who has been previously added to the transcript across tiers and in the speaker table
    get_speaker(speaker_id):
        Retrieves a speaker from the speaker table based in their speaker id
    contains_speaker(speaker_id):
        Checks if a speaker has already been added to the table of speakers
    contains_tier(tier_id):
        Checks if a tier has already been added to the list of tiers
    add_tier(speaker, tier_category='', tier_type='', display_name=''):
        Adds a tier to the record of tiers
    get_tier(tier_id):
        Returns a tier form the record of conversation tiers based on its ID
    add_event(event, speaker_id):
        Adds an Event to the transcript
    print_meta_information(indentation_level=0):
        Creates an indented xml representation of the transcript's meta information following Exmaralda standards
    print_speaker_table(indentation_level=0):
        Creates an indented xml representation of the transcript's speaker table following Exmaralda standards
    print_head(indentation_level=0):
        Creates an indented xml representation of the transcript's head following Exmaralda standards
    print_timeline(indentation_level=0):
        Creates an indented xml representation of the transcript's time line following Exmaralda standards
    print_body(indentation_level=0):
        Creates an indented xml representation of the transcript's body following Exmaralda standards
    print_transcript(indentation_level=0, with_preface=False):
        Creates an indented xml representation of the full transcript following Exmaralda standards
    """

    preface = '<?xml version="1.0" encoding="UTF-8"?>\n<!-- (c) http://www.rrz.uni-hamburg.de/exmaralda -->\n'

    def __init__(self, project_name='', transcription_name='', referenced_file_url='', ud_meta_information='',
                 comment='', transcription_convention=''):
        """
        :param project_name: name of the project
        :type project_name str (optional, defaults to '')
        :param transcription_name: transcript name  # TODO check if this might mean the person doing the transcript
        :type transcription_name str (optional, defaults to '')
        :param referenced_file_url: URL of the referenced file
        :type referenced_file_url: str (optional, defaults to '')
        :param ud_meta_information: TODO
        :type ud_meta_information: str (optional, defaults to '')
        :param comment: comments
        :type comment: str (optional, defaults to '')
        :param transcription_convention: transcription convention used
        :type transcription_convention: str (optional, defaults to '')
        """

        self.meta_information = {'project_name': project_name, 'transcription_name': transcription_name,
                     'referenced_file_url': [], 'ud_meta_information': ud_meta_information,
                     'comment': comment, 'transcription_convention': transcription_convention}
        if len(referenced_file_url.strip())>0:
            self.meta_information['referenced_file_url'].append(referenced_file_url)
        self.speaker_table = {}
        self.timeline = {}
        self.tiers = {}

    # definition of built-in methods

    def __str__(self):
        return self.print_transcript(0)

    # setter

    def set_project_name(self, project_name):
        self.meta_information['project_name'] = project_name

    def set_transcription_name(self, transcription_name):
        self.meta_information['transcription_name'] = transcription_name

    def set_referenced_file_url(self, referenced_file_url):
        self.meta_information['referenced_file_url'] = [referenced_file_url]

    def add_referenced_file_url(self, referenced_file_url):
        self.meta_information['referenced_file_url'].append(referenced_file_url)

    def set_ud_meta_information(self, ud_meta_information):
        self.meta_information['ud_meta_information'] = ud_meta_information

    def set_comment(self, comment):
        self.meta_information['comment'] = comment

    def set_transcription_convention(self, transcription_convention):
        self.meta_information['transcription_convention'] = transcription_convention

    # getter

    def get_project_name(self):
        return self.meta_information['project_name']

    def get_transcription_name(self):
        return self.meta_information['transcription_name']

    def get_referenced_file_url(self):
        return self.meta_information['referenced_file_url']

    def get_ud_meta_information(self):
        return self.meta_information['ud_meta_information']

    def get_comment(self):
        return self.meta_information['comment']

    def get_transcription_convention(self):
        return self.meta_information['transcription_convention']

    # Methods handling speaker maintenance

    def add_speaker(self, speaker_id, abbreviation='', sex='', languages_used='', l1='', l2='',
                    ud_speaker_information='', comment=''):
        """ Adds a speaker who is contributing to the converstaion to the speaker table (and tier dictionary if indicated so)

        :param speaker_id: the unique id of a speaker
        :type speaker_id: str (optional, defaults to '')
        :param abbreviation: the abbreviation used to match a turn in the transcript to a speaker
        :type abbreviation: str (optional, defaults to '')
        :param sex: the gender of the speaker
        :type sex: str (optional, defaults to '')
        :param languages_used: list of languages spoken by the speaker in the transcript
        :type languages_used: str or list of strings (optional, defaults to '')
        :param l1: first language(s) of the speaker
        :type l1: str or list of strings (optional, defaults to '')
        :param l2: str or [str], optional: second language(s) of the speaker
        :type l2: str or list of strings (optional, defaults to '')
        :param ud_speaker_information: TODO
        :type languages_used: str (optional, defaults to '')
        :param comment: comments on the speaker
        :type comment: str (optional, defaults to '')
        :param display_name: TODO
        :type display_name: str (optional, defaults to '')
        """

        if not self.contains_speaker(speaker_id):
            self.speaker_table[speaker_id] = Speaker(speaker_id, abbreviation, sex, languages_used, l1, l2, ud_speaker_information, comment)

    def overwrite_speaker(self, speaker_id, abbreviation='', sex='', languages_used='', l1='', l2='', ud_speaker_information='', comment=''):
        """ Overwrites a speaker who has been previously added to the transcript across tiers and in the speaker table

        :param speaker_id: the unique id of a speaker
        :type speaker_id: str (optional, defaults to '')
        :param abbreviation: the abbreviation used to match a turn in the transcript to a speaker
        :type abbreviation: str (optional, defaults to '')
        :param sex: the gender of the speaker
        :type sex: str (optional, defaults to '')
        :param languages_used: list of languages spoken by the speaker in the transcript
        :type languages_used: str or list of strings (optional, defaults to '')
        :param l1: first language(s) of the speaker
        :type l1: str or list of strings (optional, defaults to '')
        :param l2: str or [str], optional: second language(s) of the speaker
        :type l2: str or list of strings (optional, defaults to '')
        :param ud_speaker_information: TODO
        :type languages_used: str (optional, defaults to '')
        :param comment: comments on the speaker
        :type comment: str (optional, defaults to '')
        """

        self.speaker_table[speaker_id] = Speaker(speaker_id, abbreviation, sex, languages_used, l1, l2, ud_speaker_information, comment)

    def get_speaker(self, speaker_id):
        """ Retrieves a speaker from the speaker table based in their speaker id

        :param speaker_id: unique id of the speaker
        :type speaker_id: str
        :return: the speaker identified by the ID
        :rtype Speaker
        """

        return self.speaker_table[speaker_id]

    def contains_speaker(self, speaker_id):
        """ Checks if a speaker has already been added to the table of speakers

        :param speaker_id: unique id of the speaker
        :type speaker_id: str
        :return: true if the speaker can be found among the recorded speakers
        :rtype bool
        """

        return speaker_id in self.speaker_table.keys()

    # Methods handling tier and event maintenance

    def contains_tier(self, tier_id):
        """ Checks if a tier has already been added to the list of tiers

        :param tier_id: unique id of the tier
        :type tier_id: str
        :return: true if the tier can be found among the recorded tiers
        :rtype: bool
        """

        return tier_id in self.tiers.keys()

    # TODO define parameters
    def add_tier(self, tier_id, speaker='', tier_category='', tier_type='', display_name=''):
        """ Adds a tier to the record of tiers

        :param speaker:
        :type speaker:
        :param tier_category:
        :type tier_category:
        :param tier_type:
        :type tier_type:
        :param display_name:
        :type display_name:
        """

        if tier_id not in self.tiers.keys():
            self.tiers[tier_id] = Tier(id=tier_id, speaker=speaker, category=tier_category, type=tier_type,
                                       display_name=display_name)

    def get_tier(self, tier_id):
        """ Returns a tier form the record of conversation tiers based on its ID

        :param tier_id: unique id of the tier
        :type tier_id: str
        :return: tier associated with the ID
        :rtype: Tier
        """

        return self.tiers[tier_id]

    def add_event(self, event, tier_id):
        """ Adds an Event to the transcript

        :param event: event to be added
        :type event: Event
        """

        # add event to the tier

        if tier_id in self.tiers.keys():
            self.tiers[tier_id].add_event(event)
            # make sure time points from event begin and end are in timeline
            if event.start.time_id not in self.timeline.keys():
                self.timeline[event.start.time_id] = event.start
            if event.end.time_id not in self.timeline.keys():
                self.timeline[event.end.time_id] = event.end
        else:
            print(self.tiers.keys())

    # Printing

    def print_meta_information(self, indentation_level=0):
        """ Creates an indented xml representation of the transcript's meta information following Exmaralda standards

        :param indentation_level: current indentation level for printing within nested xml structure
        :type indentation_level: int (optional, defaults to 0)
        :return: indented xml representation of the transcript's meta data
        :rtype str
        """

        indent = '\t'*indentation_level
        rval = '{}<meta-information>'.format(indent)
        rval += '\n{}\t<project-name>{}</project-name>\n'.format(indent, self.get_project_name())
        rval += '{}\t<transcription-name>{}</transcription-name>\n'.format(indent, self.get_transcription_name())
        for ref_url in self.get_referenced_file_url():
            rval += '{}\t<referenced-file url="{}"/>\n'.format(indent, ref_url)
        rval += '{}\t<ud-meta-information>{}</ud-meta-information>\n'.format(indent, self.get_ud_meta_information())
        rval += '{}\t<comment>{}</comment>\n'.format(indent, self.get_comment())
        rval += '{}\t<transcription-convention>{}</transcription-convention>\n'.format(indent, self.get_transcription_convention())
        rval += '{}</meta-information>'.format(indent)
        return rval

    def print_speaker_table(self, indentation_level=0):
        """ Creates an indented xml representation of the transcript's speaker table following Exmaralda standards

        :param indentation_level: current indentation level for printing within nested xml structure
        :type indentation_level: int (optional, defaults to 0)
        :return: indented xml representation of the transcript's speaker table
        :rtype str
        """

        indent = '\t'*indentation_level
        rval = '{}<speakertable>'.format(indent)
        if len(self.speaker_table) == 0:
            return rval+'</speakertable>'
        rval += '\n'
        for speaker_id in sorted(self.speaker_table.keys()):
            rval += self.speaker_table[speaker_id].pretty_print(indentation_level+1)+'\n'
        return rval+'{}</speakertable>'.format(indent)

    def print_head(self, indentation_level=0):
        """ Creates an indented xml representation of the transcript's head following Exmaralda standards

        :param indentation_level: current indentation level for printing within nested xml structure
        :type indentation_level: int (optional, defaults to 0)
        :return: indented xml representation of the transcript's head
        :rtype str
        """

        indent = '\t'*indentation_level
        rval = '{}<head>'.format(indent)
        rval += '\n{}\n'.format(self.print_meta_information(indentation_level + 1))
        rval += '\n{}\n'.format(self.print_speaker_table(indentation_level+1))
        rval += '{}</head>'.format(indent)
        return rval

    def print_timeline(self, indentation_level=0):
        """ Creates an indented xml representation of the transcript's time line following Exmaralda standards

        :param indentation_level: current indentation level for printing within nested xml structure
        :type indentation_level: int (optional, defaults to 0)
        :return: indented xml representation of the transcript's time line
        :rtype str
        """

        indent = '\t'*indentation_level
        rval = '{}<common-timeline>'.format(indent)
        if len(self.timeline) == 0:
            return rval+'</common-timeline>'
        rval += '\n'+'\n'.join(self.timeline[tp_id].pretty_print(indentation_level+1) for tp_id in self.timeline.keys())
        rval += '\n{}</common-timeline>'.format(indent)
        return rval

    def print_body(self, indentation_level=0):
        """ Creates an indented xml representation of the transcript's body following Exmaralda standards

        :param indentation_level: current indentation level for printing within nested xml structure
        :type indentation_level: int (optional, defaults to 0)
        :return: indented xml representation of the transcript's body
        :rtype str
        """

        indent = '\t'*indentation_level
        rval = '{}<basic-body>'.format(indent)
        rval += '\n{}'.format(self.print_timeline(indentation_level+1))
        rval += '\n'+'\n'.join([self.tiers[tid].pretty_print(indentation_level+1) for tid in self.tiers.keys()])
        rval += '\n{}</basic-body>'.format(indent)
        return rval

    def print_transcript(self, indentation_level=0, with_preface=False):
        """ Creates an indented xml representation of the full transcript following Exmaralda standards

        :param indentation_level: current indentation level for printing within nested xml structure
        :type indentation_level: int (optional, defaults to 0)
        :param with_preface: true if the preface of the transcript should be printed
        :type with_preface: bool (optional, defaults to false)
        :return: indented xml representation of the full transcript
        :rtype str
        """

        indent = '\t'*indentation_level
        return '{}{}<basic-transcription>\n{}\n{}\n{}</basic-transcription>\n'.format(
            ExmaraldaTranscript.preface if with_preface else '',
            indent,
            self.print_head(indentation_level+1),
            self.print_body(indentation_level+1),
            indent)

    # static transcript loader

    @staticmethod
    def load(in_file):
        rval_transcript = ExmaraldaTranscript()
        tree = ET.parse(in_file)
        root = tree.getroot()

        # load meta information
        for c_info in root.iter('project-name'):
            rval_transcript.set_project_name(c_info.text.strip() if c_info.text is not None else '')
        for c_info in root.iter('transcription-name'):
            rval_transcript.set_transcription_name(c_info.text.strip() if c_info.text is not None else '')
        for c_info in root.iter('transcription-convention>'):
            rval_transcript.set_transcription_convention(c_info.text.strip() if c_info.text is not None else '')
        for c_info in root.iter('<comment>'):
            rval_transcript.set_comment(c_info.text.strip() if c_info.text is not None else '')

        # load speaker information
        for c_spk_xml in root.iter('speaker'):
            abbr = ''
            sex = ''
            lang = []
            l1 = []
            l2 = []
            comment = ''
            for c_child in c_spk_xml:
                # TODO save also ud-speaker-information
                if c_child.tag == "abbreviation" and c_child.text is not None:
                    abbr = c_child.text
                if c_child.tag == "sex" and 'value' in c_child.attrib.keys() is not None:
                    sex = c_child.attrib['value']
                if c_child.tag == "l1" and c_child.text is not None:
                    l1.append(c_child.text)
                if c_child.tag == "l2" and c_child.text is not None:
                    l2.append(c_child.text)
                if c_child.tag == "comment" and c_child.text is not None:
                    comment = c_child.text
                if c_child.tag == "languages-used" and c_child.text is not None:
                    lang.append(c_child.text)
            rval_transcript.add_speaker(speaker_id=c_spk_xml.attrib['id'], abbreviation=abbr, sex=sex,
                                        l1=l1, l2=l2, comment=comment, languages_used=lang)

        # load timelines
        for time_info in root.iter('tli'):
            new_tp = Timepoint(time_stamp=time_info.attrib['time'])
            # TODO re-think autogenerated timestamps
            new_tp.time_id = time_info.attrib['id'][1:] # overwrite the autogenerated timestamp
            rval_transcript.timeline[new_tp.time_id] = new_tp

        # load tiers and events
        for current_tier_xml in root.iter('tier'):
            c_tier_id = current_tier_xml.attrib['id'] if 'id' in current_tier_xml.attrib.keys() else ''
            rval_transcript.add_tier(tier_id=c_tier_id,
                                     speaker=current_tier_xml.attrib['speaker'] if 'speaker' in current_tier_xml.attrib.keys() else '',
                                     tier_category=current_tier_xml.attrib['category'] if 'category' in current_tier_xml.attrib.keys() else '',
                                     tier_type=current_tier_xml.attrib['type'] if 'type' in current_tier_xml.attrib.keys() else '',
                                     display_name=current_tier_xml.attrib['display-name'] if 'display-name' in current_tier_xml.attrib.keys() else '')
            for event_xml in current_tier_xml:
                if event_xml.tag != 'event':
                    print('Issue: something unexpected in tier ')
                    continue
                tp1 = Timepoint()
                tp1.set_time_id(event_xml.attrib['start'][1:])
                tp2 = Timepoint()
                tp2.set_time_id(event_xml.attrib['end'][1:])
                rval_transcript.add_event(tier_id=c_tier_id,
                                          event=Event(start=tp1, end=tp2,
                                                      content=event_xml.text if event_xml.text is not None else ''))
        return rval_transcript


# TODO put this in the test class
if __name__ == '__main__':
    """ Main method used during development """

    transcript = ExmaraldaTranscript()
    print(transcript)

    transcript.set_project_name("My Test Project")
    transcript.set_transcription_name("Exmaralda")
    transcript.set_referenced_file_url("www.url.de")
    transcript.set_ud_meta_information("12335")
    transcript.set_comment('This is nonsense. Really. Complete crab!')
    transcript.set_transcription_convention("Everything goes...")

    transcript.overwrite_speaker(speaker_id=1, abbreviation='Anna', sex='f', languages_used=['deutsch', 'englisch', 'russisch'], l1=['russisch'], l2=['deutsch', 'englisch'])
    transcript.overwrite_speaker(speaker_id=2, abbreviation='Peter', sex='m', languages_used=['deutsch', 'spanisch'], l1=['deutsch'], l2=['spanisch'])
    transcript.get_tier(1).set_display_name('Anna Karenina')
    transcript.get_tier(2).set_display_name('Peter Pan')

    counter = 1
    s = Timepoint(0.0)
    e = Timepoint(counter/10)
    transcript.add_event(Event(s, e, 'Hallo'), 2)
    s = e
    counter += 1
    e = Timepoint(counter/10)
    transcript.add_event(Event(s, e, 'Anna'), 2)
    s = e
    counter += 1
    e = Timepoint(counter/10)
    transcript.add_event(Event(s, e, '!'), 2)
    print(transcript)

    s = e
    counter += 1
    e = Timepoint(counter/10)
    transcript.add_event(Event(s, e, 'Huhu'), 1)
    s = e
    counter += 1
    e = Timepoint(counter/10)
    transcript.add_event(Event(s, e, 'Peter'), 1)
    s = e
    counter += 1
    e = Timepoint(counter/10)
    transcript.add_event(Event(s, e, '!'), 1)

    s = e
    counter += 1
    e = Timepoint(counter/10)
    transcript.add_event(Event(s, e, 'YOLO'), 2)

    print(transcript)
    print(transcript.print_transcript(with_preface=True))
