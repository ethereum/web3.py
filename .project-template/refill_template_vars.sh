TEMPLATE_DIR=$(dirname $(readlink -f "$0"))
<"$TEMPLATE_DIR/template_vars.txt" "$TEMPLATE_DIR/fill_template_vars.sh"
