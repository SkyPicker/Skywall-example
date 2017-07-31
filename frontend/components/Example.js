import React from 'react'
import {compose} from 'redux'
import {applyOverlays} from 'skywall/frontend/utils/overlays'


export class ExampleComponent extends React.Component {

  static propTypes = {
  }

  render() {
    return (
      <div>
        <p>Example</p>
      </div>
    )
  }
}

export default compose(
  applyOverlays,
)(ExampleComponent)
