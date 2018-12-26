.. image:: https://raw.githubusercontent.com/bmjjr/modality/master/img/modality_img.jpg?token=AAgJc9an2d8HwNRHty-6vMZ94VfUGGSIks5b8VHbwA%3D%3D

**A framework for creating hardware product test suites.**

.. image:: https://img.shields.io/badge/Python-3.6%20%7C%203.7-blue.svg
  :target: https://github.com/bomquote/modality
.. image:: https://img.shields.io/badge/Status-Alpha-yellow.svg
  :target: https://github.com/bomquote/modality
.. image:: https://img.shields.io/badge/license-MIT-lightgrey.svg
  :target: https://github.com/bomquote/modeality/blob/master/LICENSE


=============
*Modality*
=============

About
-----

**Alpha concept development. Not currently usable.**

Modality is a framework which supports hardware product specification, analysis,
design, verification, and validation in the new product development process,
as viewed from a systems engineering perspective.

It integrates concepts from `MBSE (Model Based Systems Engineering) <https://en.wikipedia.org/wiki/Model-based_systems_engineering>`_ and OOSEM
(Object-Oriented Systems Engineering Method) along with `Sys.ML
(Systems Modeling Language) <https://sysml.org/sysml-faq/>`_ to enable describing simple to complex systems that
may include hardware, software, data, personnel, procedures, and facilities.

Ultimately, it's core use case is to assist in building test suites used for
product design verification, validation, unit, and system testing.

Development of Modality is sponsored by `BOM Quote Manufacturing <https://www.bomquote.com>`_.


Goals
----------

Modality should be useful to developers to build test suites for those involved
in hardware design, product development, or product lifecycle management for
hardware products.

The framework should help to create test suites used to:

- verify specifications realize intended product features
- generate actionable tests, for engineering or MFG QA use

Particularly, it should be useful to develop test suites for:

1. highlighting related change areas in a change process
2. adding new features to existing designs
3. design verification and validation testing
4. performing functional and/or acceptance testing

Motivation
----------

For example, in the 'NPI' or 'New Product Introduction' phase. Design changes must
often be made to realize features or to improve manufacturability. Even when using
a clear ECR/ECO process, without a standard test framework in place customized to
the product, it is easy to make mistakes and oversights. Especially, when working
with external suppliers or CM's. Mistakes and oversights result in project delays.

Also, when hardware designers work with external teams, like a CM team, the CM team
must come up to speed on the design. But, it is difficult for non-dedicated staff
who were not involved in the design process to fully comprehend a hardware product
as a system. Clearly defined test suites for subassembly and system reviews are
helpful if they exist. But, usually early in the design phase they do not exist
and how to go about creating them is non-standard.

Generally, a reliance on individual talents and heroics of individuals and
the responsible designers is how these issues are overcome. Test suites built
with Modality should help to reduce reliance on individual heroics and instead
help to formalize a standardized process for tests and system reviews.

Common types of issues that test suites built with Modality should help address
include:

Technical Oversights

- Making a change but missing related changes that should be made in other areas
- Making changes but then failing to assess the impact to the system as a whole

Unclear Specifications

- Failing to appropriately specify each individual part in a BOM
- Failing to specify modules and subassemblies comprised of parts
- Failing to adequately specify the system for testing

Unclear Relations

- Failing to formally identify interconnected parts and dependencies


Terminology
------------

Design verification is defined as, "confirmation by examination and provision of
objective evidence that specified requirements have been fulfilled."

Design validation is, "establishing by objective evidence that device specifications
conform with user needs and intended use(s)."

Simply put, verification confirms that the design output meets the design input
requirements, while validation ensures that user needs are met by the product.


System/Subsystem:
A `system` means a product.  `Subsystems` mean parts that compose the product.

.. image:: https://raw.githubusercontent.com/bmjjr/modality/master/img/system_subsystem.jpg?token=AAgJc9an2d8HwNRHty-6vMZ94VfUGGSIks5b8VHbwA%3D%3D


Control model/Plant model:
`Subsystems` are categorized into two types:

1. control models which control subsystems
2. plant models which are controlled by control models

.. image:: https://raw.githubusercontent.com/bmjjr/modality/master/img/control_model_plant_model.jpg?token=AAgJc9an2d8HwNRHty-6vMZ94VfUGGSIks5b8VHbwA%3D%3D


Interface:
An `interface` means a relation between plant models in a subsystem.

.. image:: https://raw.githubusercontent.com/bmjjr/modality/master/img/subsystem_interfaces.jpg?token=AAgJc9an2d8HwNRHty-6vMZ94VfUGGSIks5b8VHbwA%3D%3D


