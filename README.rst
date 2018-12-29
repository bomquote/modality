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

**Pre-Alpha concept development. Not currently usable.**

Modality is a framework which supports Model Based Testing (MBT) for hardware products.

It's goal is to be useful to guide specification, analysis, design, verification, and
validation testing in the new product development process, as viewed from a systems
engineering perspective.

Particularly, it should be useful to develop a quick, accurate understanding of how
a design change will impact the requirements of other aspects of the product
as a system.

It integrates concepts from `MBSE (Model Based Systems Engineering) <https://mbseworks.com/mbse-overview/>`_ and `Sys.ML
(Systems Modeling Language) <https://sysml.org/sysml-faq/>`_ to enable describing simple to complex systems that
may include hardware, software, data, personnel, procedures, and facilities.

Practically, it's core use case is to first use SysML to build models which are then used to
build test suites for product design verification, validation, unit, and system testing.

Development of Modality is sponsored by `BOM Quote Manufacturing <https://www.bomquote.com>`_.


Goals
----------

Modality should be useful to developers to build models of systems under consideration
(SUC). The system requirements and interface relations are then used to build test
suites for the SUC. Targeted users are those involved in hardware design, product
development, or product lifecycle management for products viewed as a system, including
moderately complex hardware (electronic + mechanical) + software (embedded) systems.

The framework should help to create test suites used to:

- verify specifications realize intended product features
- generate actionable tests, for engineering or MFG QA use

Particularly, it should be useful to develop test suites to:

1. highlight potential related change areas to consider in a change process
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
as a system. Clearly defined test suites for subassembly and system requirement
documents are helpful if they exist. But, usually early in the design phase they do
not exist and how to go about creating them is non-standard.

Generally, a reliance on individual talents and heroics of the responsible designers
is how these issues are overcome. Test suites built with Modality should help to
reduce reliance on individual heroics and instead help to formalize a standardized
process for tests and system reviews.

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


Acronyms:

- SUC : System under consideration


Model Based Testing:

A lightweight formal method which is used to validate a system.
Such testing method is applicable to both hardware and software testing. We use the
system requirements in order to generate the efficient test cases with the help of a
Model. Given below is an overview of a model based testing.

- Develop a model.
- Determine various inputs for this model.
- Determine expected output for this model.
- Execute the tests.
- Compare the returned result against the expected output.
- Make the decision on the action on the model.

