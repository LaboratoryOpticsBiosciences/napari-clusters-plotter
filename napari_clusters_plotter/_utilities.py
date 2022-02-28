import pandas as pd


def widgets_inactive(*widgets, active):
    for widget in widgets:
        widget.setVisible(active)


def show_table(viewer, labels_layer):
    from napari_skimage_regionprops import add_table

    add_table(labels_layer, viewer)


def restore_defaults(widget, defaults: dict):
    for item, val in defaults.items():
        getattr(widget, item).value = val


def set_features(layer, tabular_data):
    if hasattr(layer, "properties"):
        layer.properties = tabular_data
    if hasattr(layer, "features"):
        layer.features = tabular_data


def get_layer_tabular_data(layer):
    if hasattr(layer, "properties") and layer.properties is not None:
        return pd.DataFrame(layer.properties)
    if hasattr(layer, "features") and layer.features is not None:
        return layer.features
    return None

def add_column_to_layer_tabular_data(layer, column_name, data):
    if hasattr(layer, "properties"):
        layer.properties[column_name] = data
    if hasattr(layer, "features"):
        layer.features[column_name] = data

def get_nice_colormap():
    colours_w_old_colors = [
        "#ff7f0e",
        "#1f77b4",
        "#2ca02c",
        "#d62728",
        "#9467bd",
        "#8c564b",
        "#e377c2",
        "#7f7f7f",
        "#bcbd22",
        "#17becf",
        "#ccebc5",
        "#ffed6f",
        "#0054b6",
        "#6aa866",
        "#ffbfff",
        "#8d472a",
        "#417239",
        "#d48fd0",
        "#8b7e32",
        "#7989dc",
        "#f1d200",
        "#a1e9f6",
        "#924c28",
        "#dc797e",
        "#b86e85",
        "#79ea30",
        "#4723b9",
        "#3de658",
        "#de3ce7",
        "#86e851",
        "#9734d7",
        "#d0f23c",
        "#3c4ce7",
        "#93d229",
        "#8551e9",
        "#eeea3c",
        "#ca56ee",
        "#2af385",
        "#ea48cd",
        "#7af781",
        "#7026a8",
        "#51d967",
        "#ad3bc2",
        "#4ab735",
        "#3b1784",
        "#afc626",
        "#3d44bc",
        "#d5cc31",
        "#6065e6",
        "#8fca40",
        "#9e2399",
        "#27ca6f",
        "#e530a4",
        "#54f2ad",
        "#c236aa",
        "#a1e76b",
        "#a96fe6",
        "#64a725",
        "#d26de1",
        "#52b958",
        "#867af4",
        "#ecbe2b",
        "#4f83f7",
        "#bbd14f",
        "#2f65d0",
        "#ddf47c",
        "#27165e",
        "#92e986",
        "#8544ad",
        "#91a824",
        "#2e8bf3",
        "#ec6e1b",
        "#2b6abe",
        "#eb3e22",
        "#43e8cf",
        "#e52740",
        "#5ef3e7",
        "#ed2561",
        "#6ceac0",
        "#681570",
        "#8eec9c",
        "#8f2071",
        "#add465",
        "#3a4093",
        "#e3ce58",
        "#5a3281",
        "#82bf5d",
        "#e1418b",
        "#3d8e2a",
        "#e86ec2",
        "#66ca7d",
        "#ae1e63",
        "#4abb81",
        "#dc3b6c",
        "#409e59",
        "#b34b9d",
        "#87a943",
        "#958df3",
        "#e59027",
        "#667edb",
        "#ddad3c",
        "#545daf",
        "#e4e68b",
        "#22123e",
        "#b9e997",
        "#6c2c76",
        "#b0c163",
        "#866ecb",
        "#5f892d",
        "#d889e2",
        "#276222",
        "#ab98ed",
        "#79801a",
        "#8f5baa",
        "#ab972e",
        "#7899e9",
        "#dc5622",
        "#4a9de3",
        "#bd2e10",
        "#54d5d6",
        "#bc2f25",
        "#40bd9c",
        "#c72e45",
        "#9ae5b4",
        "#891954",
        "#d6ecb1",
        "#0e0d2c",
        "#e9c779",
        "#193163",
        "#f07641",
        "#4ab5dc",
        "#e35342",
        "#6dd3e7",
        "#92230d",
        "#a3e9e2",
        "#951a28",
        "#48a7b4",
        "#a8421a",
        "#88c4e9",
        "#c55a2b",
        "#2e5c9d",
        "#bb8524",
        "#737bc6",
        "#c2bc64",
        "#661952",
        "#92bc82",
        "#46123b",
        "#d6e5c8",
        "#190b1f",
        "#e5a860",
        "#1d1d3c",
        "#f27c58",
        "#06121f",
        "#ebcfa3",
        "#06121f",
        "#f3a27d",
        "#06121f",
        "#eb6065",
        "#297a53",
        "#af437c",
        "#365412",
        "#be9ee2",
        "#636b24",
        "#e9a1d5",
        "#1c2c0c",
        "#e3bce6",
        "#06121f",
        "#cf8042",
        "#06121f",
        "#bfdee0",
        "#751718",
        "#80c1ab",
        "#bb3f44",
        "#2b9083",
        "#781731",
        "#618d58",
        "#93457c",
        "#7f954c",
        "#4b2a5c",
        "#c3bd83",
        "#290d1b",
        "#ced0ec",
        "#6a2d0a",
        "#9db5ea",
        "#a35c1b",
        "#4781b1",
        "#9e4e22",
        "#33547a",
        "#876a1c",
        "#514e80",
        "#a59952",
        "#b86198",
        "#1d3621",
        "#eb7ba2",
        "#002a33",
        "#e38273",
        "#17212e",
        "#e8c4c5",
        "#281c2e",
        "#b3b18a",
        "#581430",
        "#659c84",
        "#a23a50",
        "#2d7681",
        "#a44634",
        "#608ea2",
        "#783121",
        "#94a9bc",
        "#4b1615",
        "#a4ae9f",
        "#7c3258",
        "#aa8242",
        "#7a6ea2",
        "#5f5621",
        "#c27dae",
        "#403911",
        "#a499c7",
        "#805124",
        "#717e9e",
        "#b8644f",
        "#143b44",
        "#ce6472",
        "#142a25",
        "#dd9ca6",
        "#21344a",
        "#d7a78c",
        "#3c3551",
        "#928853",
        "#ad486c",
        "#3a4d2d",
        "#8c5481",
        "#516b4d",
        "#994440",
        "#2e5667",
        "#af7e5c",
        "#432432",
        "#b49bb0",
        "#382718",
        "#b67576",
        "#294d46",
        "#935c54",
        "#52756e",
        "#6d363c",
        "#85856a",
        "#644466",
        "#635738",
        "#876d84",
        "#623c23",
        "#596776",
        "#864e5d",
        "#5f5848",
        "#9f7e80",
        "#5c4a56",
        "#735647",
        "#bcbcbc",
    ]

    return colours_w_old_colors
