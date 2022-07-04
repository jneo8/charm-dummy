# Workshop

## Key points:

### Brief introduction to zaza

- Go over the stages of zaza test execution (prepare, deploy, configure, test, …)
- Explain why are OS functional tests in separate repository
    > This is a test library designed to be shared between the OpenStack Charms to improve code-reuse among the various components.
    >
    >   [openstack-charmers/zaza-openstack-tests](https://github.com/openstack-charmers/zaza-openstack-tests/blob/master/README.md)

- How to link PR in opendev.org to a custom branch of zaza openstack tests (?)

- Checkout charm and our branch of zaza-openstack-tests
  `./src/test-requirements.txt`

  ```
  ...

  # Functional Test Requirements (let Zaza's dependencies solve all dependencies here!)
  git+https://github.com/openstack-charmers/zaza.git@stable/yoga#egg=zaza
  git+https://github.com/jneo8/zaza-openstack-tests.git@feat/dummy-test#egg=zaza.openstack

  ...
  ```

- Inspect already existing “dummy” test
    - Where are the tests placed?
        ```bash
        cd ./src/.tox/func-target/lib/python3.8/site-packages/zaza/
        ```
    - Where are the custom configuration functions placed?
        - https://github.com/jneo8/zaza-openstack-tests/tree/feat/dummy-test/zaza/dummy/configure
    - Where is the testing bundle?
        - `./src/tests/bundles`
    - How to tell charm which bundle to use, which configuration steps to run and which tests to execute?
        ```bash
        cat ./src/tests/tests.yaml
        ```
- Execute the existing “dummy” functional tests to confirm that we have a working environment
    - Explain how to make sure that the testing model won’t be destroyed as we’ll be using it later
        ```bash
        functest-run-suite --keep-model --bundle focal
        ```
- Start working on our new tests for the dummy charm
    - Create new class for tests (explain why it’s a best practice to always add tests into new class)
    - Add test(s) that utilize some of the interesting zaza features
        - Run action
        - Run command on unit
        - Check unit/application status
        - ???
    - Possibly include a minor mistake in our test so that the test run (next step) will fail and we’ll have to come back, fix the problem and re-run tests (?)
- Run our new tests on existing model
    - Inject our zaza-openstack-tests into the virtual environment
    - Use functest-test to run our tests
        - Briefly explain other functest-* commands


## References


### Relate projects 

[juju-solutions/charms.reactive](https://github.com/juju-solutions/charms.reactive)
[juju-solutions/layer-basic](https://github.com/juju-solutions/layer-basic)
[juju/charm-helpers](https://github.com/juju/charm-helpers)
[zaza](https://github.com/openstack-charmers/zaza)
[openstack/charms.openstack](https://github.com/openstack/charms.openstack)
[openstack-charmers/zaza-openstack-tests](https://github.com/openstack-charmers/zaza-openstack-tests)
[openstack-charmers/release-tools](https://github.com/openstack-charmers/release-tools)
