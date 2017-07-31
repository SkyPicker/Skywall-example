import React from 'react'
import {Table} from 'react-bootstrap'
import {ClientListTableComponent} from 'skywall/frontend/components/ClientListTable'
import {registerOverlay} from 'skywall/frontend/utils/overlays'
import {findElements, appendChildren} from 'skywall/frontend/utils/traverse'


registerOverlay(ClientListTableComponent, (rendered) => {
  let res = rendered
  res = findElements(res, [Table, 'thead', 'tr'], (node) => {
    return appendChildren(node,
      <th key="example">Example</th>
    )
  })
  res = findElements(res, [Table, 'tbody', 'tr'], (node) => {
    const clientId = node.props['data-clientId']
    return appendChildren(node,
      <td key="example">Example {clientId}</td>
    )
  })
  return res
})
