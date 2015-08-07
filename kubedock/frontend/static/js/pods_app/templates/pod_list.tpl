<div class="col-md-12">
    <div class="podsControl">
        <span class="count"></span>
        <span class="runPods">Run</span>
        <span class="stopPods">Stop</span>
        <span class="removePods">Delete</span>
    </div>
    <table id="podlist-table" class="table tablesorter tablesorter-default">
        <thead>
            <tr class="tablesorter-headerRow">
                <th data-column="0" class="tablesorter-header tablesorter-headerDesc" tabindex="0" unselectable="on" style="-webkit-user-select: none;">
                    <div class="tablesorter-header-inner">
                        <label class="custom">
                            <input type="checkbox">
                            <span></span>
                        </label>
                    </div>
                </th>
                <th data-column="1" class="tablesorter-header tablesorter-headerDesc" tabindex="0" unselectable="on" style="-webkit-user-select: none;">
                    <div class="tablesorter-header-inner">
                        <b class="caret"></b>
                    </div>
                </th>
                <th data-column="2" class="tablesorter-header" tabindex="0" unselectable="on" style="-webkit-user-select: none;">
                    <div class="tablesorter-header-inner">Pod name<b class="caret"></b></div>
                </th>
                <th data-column="4" class="tablesorter-header" tabindex="0" unselectable="on" style="-webkit-user-select: none;">
                    <div class="tablesorter-header-inner">Replicated<b class="caret"></b></div>
                </th>
                <th data-column="5" class="tablesorter-header" tabindex="0" unselectable="on" style="-webkit-user-select: none;">
                    <div class="tablesorter-header-inner">Status<b class="caret"></b></div>
                </th>
                <th data-column="6" class="tablesorter-header" tabindex="0" unselectable="on" style="-webkit-user-select: none;">
                    <div class="tablesorter-header-inner">Kube type<b class="caret"></b><br/>(kubes quantity)</div>
                </th>
            </tr>
        </thead>
        <tbody></tbody>
    </table>
</div>
