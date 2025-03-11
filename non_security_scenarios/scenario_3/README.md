# Non-security scenario 3

## Requirements

Packages:

```plaintext
rti_connext_dds-6.1.2-pro-host-<architecture>.<run/exe>
rti_real_time_wan_transport-6.1.2-host-<architecture>.rtipkg
```

With regards to network configuration, you'll need to add a security rule on
your AWS instance to allow incoming / outgoing traffic on PUBLIC_PORT, for the
UDP protocol. For instance:

![AWS Configuration](../../resources/images/configuration_aws.png)

## Diagram

![Non-security scenario 3 diagram](../../resources/images/non_security_scenario_3.png)

The AWS Passive Routing Service will listen for incoming communications. The
Active Routing Services will use their initial peers to start the communication
with the Passive one. AWS's Routing Service will relay the communication. In the
diagram above, the public address needs to be known by the remote Active
Routing Services.

## How to run this scenario

On AWS:

1. In a terminal, set up NDDSHOME pointing at the Connext installation and set these variables:

    ```bash
    export PUBLIC_ADDRESS=<public_IP_address>
    export PUBLIC_PORT=<PUBLIC_PORT>
    export INTERNAL_PORT=<INTERNAL_PORT>
    ```

2. Run Routing Service:

    ```bash
    cd non_security_scenarios/scenario_3/
    $NDDSHOME/bin/rtiroutingservice -cfgFile RsConfig_Cloud.xml -cfgName RsConfig_Cloud
    ```

On Home Office 1:

1. Start a Shapes Demo publisher on domain 1. Publish some shapes.
2. In a terminal, set up NDDSHOME pointing at the Connext installation and set these variables:

    ```bash
    export PUBLIC_ADDRESS=<public_IP_address>
    export PUBLIC_PORT=<PUBLIC_PORT>
    ```

3. Run Routing Service:

    ```bash
    cd non_security_scenarios/scenario_3/
    $NDDSHOME/bin/rtiroutingservice -cfgFile RsConfig_Local.xml -cfgName RsConfig_Local
    ```

On Home Office 2:

1. Start a Shapes Demo subscriber on domain 1. Subscribe to some shapes.
2. In a terminal, set up NDDSHOME pointing at the Connext installation and set these variables:

    ```bash
    export PUBLIC_ADDRESS=<public_IP_address>
    export PUBLIC_PORT=<PUBLIC_PORT>
    ```

3. Run Routing Service:

    ```bash
    cd non_security_scenarios/scenario_3/
    $NDDSHOME/bin/rtiroutingservice -cfgFile RsConfig_Local.xml -cfgName RsConfig_Local
    ```

## Expected output

After some seconds, once discovery is completed, Home Office 2 should start
receiving the shapes that Home Office 1 publishes. Actually, you could start
any number of Shapes Demo publishers on either side and the other one should
receive those, as well. Routing Service helps with scalability because you do
not need to initiate new WAN connections per application, you just need Routing
Service to take care of that for you.
