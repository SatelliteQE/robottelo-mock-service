# robottelo-mock-service

[![Copr build status](https://copr.fedorainfracloud.org/coprs/ogajduse/robottelo-mock-service/package/robottelo-mock-service/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/ogajduse/robottelo-mock-service/package/robottelo-mock-service/)

This package provides simple mock service that serves for
katello-tracer testing in robottelo.


## How to build the package

```
make
```

To install it:
```
make install
```

To build a source RPM:
```
tito build --test --srpm
```

And to build RPM package:
```
mock --rebuild <path-to-srpm>
```

Or use a shortcut:
```
tito build --rpm --builder=mock --arg=mock=epel-9-x86_64
```

## How to release a new verison

Commit all changes to SCM and create a new tag using tito.
```
tito tag
```

Push the commit created by `tito tag` and the tag itself to the upstream repository.

This will create a new commit in which the version in the SPEC file is bumped and a new changelog entry was appended.

To submit a new build on Fedora Copr, run the following command
```
tito release copr
```

SRPM will get uploaded to COPR and a new build will be submitted.
The version to be built depends on the version specified in
`.tito/packages/robottelo-mock-service`.

## Authors
Ondrej Gajdusek <ogajduse@redhat.com>

Roman Plevka <rplevka@redhat.com>


