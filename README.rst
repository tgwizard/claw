claw
====

.. image:: https://circleci.com/gh/tictail/claw.svg?style=svg
    :target: https://circleci.com/gh/tictail/claw

Claw, https://github.com/tictail/claw, is a library to extract message quotations and signatures.
It is is a more light-weight version of the original https://github.com/mailgun/talon library.

`Changelog <https://github.com/tictail/claw/blob/master/CHANGELOG.md>`_

If you ever tried to parse message quotations or signatures you know that absence of any formatting standards in this area could make this task a nightmare.
Hopefully this library will make your life much easier.

Installation
------------

.. code::

    pip install claw



Usage
-----

Here’s how you initialize the library and extract a reply from a text
message:


.. code:: python

    import claw
    from claw import quotations
    
    claw.init()
    
    text =  """Reply
    
    -----Original Message-----
    
    Quote"""
    
    reply = quotations.extract_from(text, 'text/plain')
    reply = quotations.extract_from_plain(text)
    # reply == "Reply"


To extract a reply from html:

.. code:: python

    html = """Reply
    <blockquote>
    
      <div>
        On 11-Apr-2011, at 6:54 PM, Bob &lt;bob@example.com&gt; wrote:
      </div>
    
      <div>
        Quote
      </div>
    
    </blockquote>"""
    
    reply = quotations.extract_from(html, 'text/html')
    reply = quotations.extract_from_html(html)
    # reply == "<html><body><p>Reply</p></body></html>"


Often the best way is the easiest one. Here’s how you can extract
signature from email message without any
machine learning fancy stuff:

.. code:: python

    from claw.signature import extract_signature
    
    
    message = """Wow. Awesome!
    --
    Bob Smith"""
    
    text, signature = extract_signature(message)
    # text == "Wow. Awesome!"
    # signature == "--\nBob Smith"


Quick and works like a charm 90% of the time. For other 10% you can use
the power of machine learning algorithms. See the original talon implementation.


Development
-----------

.. code::

    virtualenv venv
    source venv/bin/activate
    
    make install
    
    make test


Release new version:

Bump the version in setup.py and update CHANGELOG.md, and then:

.. code::

    make release
