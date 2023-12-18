<script>
    let converted = "";
    let convert = async () => {
        let clipboard = await navigator.clipboard.readText();
        console.log(clipboard);
        let waypoints = clipboard.split("\n");
        let waypointsarr = [];
        waypoints.forEach(waypoint => {
            waypoint = waypoint.replaceAll("\r", "");
            waypoint = waypoint.replace("/sthw set ", "");
            let waypoint_split = waypoint.split(" ");
            waypointsarr.push({
                name: waypoint_split[3],
                x: waypoint_split[0],
                y: waypoint_split[1],
                z: waypoint_split[2],
                enabled: true,
                addedAt: Date.now()
            });
        })
        waypointsarr.pop();
        let name = "Parsed Waypoints";
        let island = "crystal_hollows";
        let txt_ = JSON.stringify({
            "categories": [{name: name, waypoints: waypointsarr, island: island}]
        })
        converted = txt_
        // converted = txt;
    }

</script>
<main>
    <h1>Convert Skytils /sthw commands to Import from Clipboard</h1>
    <p>If this does not work, make sure you have enabled read from clipboard. If you do not trust this, read the code at <a href="https://github.com/Westsi/skytils-converter-site">Github</a>.</p>
    <p>Uses coords in format /sthw set &lt;x&gt; &lt;y&gt; &lt;z&gt; &lt;name&gt;. Make sure your coords are in that form.</p>
    <button on:click={convert}>Convert from Clipboard</button>
    <h2>Output Encoded</h2>
    <textarea class="long">{btoa(converted)}</textarea>
    <br>
    <br>
    <h3>Output JSON</h3>
    <textarea class="long">{converted}</textarea>
</main>

<style>
    main {
        text-align: center;
        background-color: #242424;
    }
    h1 {
        text-align: center;
    }
    .long {
        width: 80%;
        height: 400px;
    }
</style>
