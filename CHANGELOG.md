### v1.3.0 2015-09-16

 - Better support for Scandinavian languages: [GH-6](https://github.com/tictail/claw/pull/6).

### v1.2.0 2015-08-25

 - Strip last root-level `<blockquote>` instead of first when parsing HTML replies: [GH-4](https://github.com/tictail/claw/pull/4).

### v1.1.0 2015-08-25

 - Better support for German reply headers: [GH-2](https://github.com/tictail/claw/pull/2).

### v1.0.1 2015-08-23

 - Fixed bug when parsing replies from Apple Mail, where a trailing `>` would be included: [GH-1](https://github.com/tictail/claw/pull/1).

### v1.0.0 2015-08-22

First version of claw released, forked off from talon v1.0.2.

 - Removed the machine learning code and depdenencies on numpy and PyML. This reduced installation footprint considerably.
 - Removed install dependencies on chardet, dnspython, nose, mock, coverage and flanker
 - Renamed to claw, moved to py.test.
