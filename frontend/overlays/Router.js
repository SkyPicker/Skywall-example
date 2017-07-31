import React from 'react'
import {Route} from 'react-router'
import WithMenu from 'skywall/frontend/components/WithMenu'
import {RouterComponent} from 'skywall/frontend/components/Router'
import {registerOverlay} from 'skywall/frontend/utils/overlays'
import {isElement, traverse, appendChildren} from 'skywall/frontend/utils/traverse'
import * as routes from '../constants/routes'
import Example from '../components/Example'


registerOverlay(RouterComponent, (rendered) => {
  let res = rendered
  res = traverse(res, (node, path, traverseIn) => {
    if (isElement(node) && node.props.component === WithMenu) {
      return appendChildren(node, [
        <Route key="example" path={routes.EXAMPLE} component={Example} />,
      ])
    }
    return traverseIn(node, path)
  })
  return res
})
